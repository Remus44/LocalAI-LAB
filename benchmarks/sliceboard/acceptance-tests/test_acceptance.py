"""Operator-only tests. Run with PYTHONPATH pointing to candidate workspace.
Set SLICE=1,2,3,4 to validate cumulative behavior. Never provide to worker."""
import unittest
import tempfile
import pathlib
import os
import json
import subprocess
import sys
from sliceboard.models import TaskManager

SLICE=int(os.getenv("SLICE","4"))

class Domain(unittest.TestCase):
    def test_domain(self):
        m=TaskManager()
        a=m.add("  one  ")
        self.assertEqual((a.id,a.title,a.status),(1,"one","pending"))
        self.assertEqual(m.get(1),a)
        self.assertIsNone(m.get(999))
        with self.assertRaises(ValueError): m.add(" ")
        with self.assertRaises(ValueError): m.update_status(1,"bad")
        with self.assertRaises(KeyError): m.update_status(999,"done")
        self.assertEqual(m.update_status(1,"done").status,"done")
        self.assertTrue(m.delete(1))
        self.assertFalse(m.delete(1))
        self.assertEqual(m.add("two").id,2)
        self.assertEqual([x.id for x in m.list_tasks()],[2])

@unittest.skipUnless(SLICE>=2,"S02 not yet assigned")
class Persistence(unittest.TestCase):
    def test_roundtrip(self):
        from sliceboard.storage import save_tasks,load_tasks
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/"state.json"
            m=load_tasks(p)
            self.assertEqual(m.list_tasks(),[])
            m.add("one");m.add("two");m.update_status(2,"done");m.delete(1)
            save_tasks(m,p)
            n=load_tasks(p)
            self.assertEqual([(x.id,x.title,x.status) for x in n.list_tasks()],[(2,"two","done")])
            self.assertEqual(n.add("three").id,3)
            for invalid in ["{",json.dumps({"version":2,"next_id":1,"tasks":[]}),json.dumps({"version":1,"next_id":1,"tasks":[{"id":1,"title":"x","status":"pending"}]})]:
                p.write_text(invalid,encoding="utf-8")
                with self.assertRaises(ValueError):load_tasks(p)

@unittest.skipUnless(SLICE>=3,"S03 not yet assigned")
class CLI(unittest.TestCase):
    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/"state.json"
            def run(*args):
                return subprocess.run([sys.executable,"-m","sliceboard.cli","--file",str(p),*args],capture_output=True,text=True,timeout=15)
            self.assertEqual(run("add","first").returncode,0)
            self.assertIn("1 | pending | first",run("list").stdout)
            self.assertEqual(run("status","1","done").returncode,0)
            self.assertIn("1 | done | first",run("list").stdout)
            before=p.read_bytes()
            bad=run("status","1","bad")
            self.assertNotEqual(bad.returncode,0)
            self.assertTrue(bad.stderr)
            self.assertEqual(p.read_bytes(),before)
            self.assertEqual(run("delete","1").returncode,0)
            self.assertEqual(run("add","second").returncode,0)
            self.assertIn("2 | pending | second",run("list").stdout)
            if SLICE>=4:
                self.assertNotIn("second",run("list","--status","done").stdout)
                self.assertIn("second",run("list","--status","pending").stdout)
                self.assertNotEqual(run("list","--status","bad").returncode,0)
                summary=run("summary")
                self.assertEqual(summary.returncode,0)
                for line in ["Total: 1","Pending: 1","In progress: 0","Done: 0"]:
                    self.assertIn(line,summary.stdout)

@unittest.skipUnless(SLICE>=4,"S04 not yet assigned")
class Filtering(unittest.TestCase):
    def test_filter(self):
        m=TaskManager()
        m.add("a");m.add("b");m.update_status(2,"done")
        self.assertEqual([t.id for t in m.list_tasks("done")],[2])
        self.assertEqual(len(m.list_tasks()),2)
        with self.assertRaises(ValueError):m.list_tasks("bad")

if __name__=="__main__":
    unittest.main()
