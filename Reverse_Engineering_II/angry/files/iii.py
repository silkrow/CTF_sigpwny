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
	# add_options = angr.options.unicorn
)

for b in arg1.chop(8):
	state.add_constraints(b >= ord('!'))
	state.add_constraints(b <= ord('~'))

sm = proj.factory.simulation_manager(state)

#### METHOD 1 ####

#sm.explore(find = success, avoid = fail)
#print(sm.found[0].solver.eval(arg1, cast_to=bytes))

#### END OF METHOD 1 ####

#### METHOD 2 ####

iter_num = 0

def find_condition(state):
	if (state.addr == for_success and state.solver.eval(state.regs.eax) == iter_num):
		return True
	else:
		return False

for i in range(31):
	iter_num = i
	print(i)
	print(sm.active[0].solver.eval(arg1, cast_to=bytes))
	print(sm.active[0].regs.eax)
	sm.explore(find=find_condition, avoid=fail).move(from_stash='found', to_stash='active')
	temp_s = sm.active[0].solver.eval(arg1.get_byte(i), cast_to = bytes)
	print(temp_s)
	sm.active[0].add_constraints(arg1.get_byte(i) == temp_s)

s = sm.active[0]
print("Done!")
print(s.solver.eval(arg1,cast_to=bytes))

#### END OF METHOD 2 ####
