import logging
import angr
import claripy

# logging.getLogger('angr.sim_manager').setLevel('DEBUG')

len_fail = 0x004052ec
success = 0x0040547d
fail = 0x0040544f
for_success = 0x00405465

proj = angr.Project("./angry")

arg1 = claripy.BVS('arg1', 31*8)

state = proj.factory.entry_state(
	args=['angry', arg1],
	add_options = angr.options.unicorn
)

for b in arg1.chop(8):
	state.add_constraints(b >= ord('!'))
	state.add_constraints(b <= ord('~'))

sm = proj.factory.simulation_manager(state)


sm.explore(find = success, avoid = fail)
print(sm.found[0].solver.eval(arg1, cast_to=bytes))
