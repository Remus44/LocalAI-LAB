# Operator rubric
AT01: empty=0, [{price:3,quantity:2}]=6, invalid price/quantity ValueError, input unchanged.
AT02: [1,3,2]→2; [5,5,3]→3; [7,7],[]→None; [-5,-2,-1]→-2; input unchanged.
AT03: tests execute against correct implementation and detect boundary/invalid-range mutants.
AT04: both exact locations/codes; no invented source.
AT05: all facts in report, no invented smoke result or decisions.
AT06: removed negative validation, unauthorized config change, no test changes shown, no claims of execution.
AT07: {"completed_slices":["S01"],"active_slice":"S02","build_passed":true,"smoke_tests_passed":null}
AT08: BLOCKED; missing discount rules.
