import logging
import angr
import claripy

# logging.getLogger('angr.sim_manager').setLevel('DEBUG')

len_fail = 0x004052ec
success = 0x0040547d
fail = 0x0040544f
for_success = 0x00405465

known = []
iter_num = 0

def find_condition(state):
	if (state.addr == for_success and state.solver.eval(state.regs.eax) == iter_num):
		return True
	else:
		return False

for i in range(31):
	iter_num = i
	print('round: ' + str(i))
	print(known)

	proj = angr.Project("./angry")
	arg1 = claripy.BVS('arg1', 31*8)

	ent_state = proj.factory.entry_state(args=['angry', arg1])	

#	for b in arg1.chop(8):
#		ent_state.add_constraints(b >= ord('!'))
#		ent_state.add_constraints(b <= ord('~'))
	
	if (i > 0):
		for j in range(len(known)):
			ent_state.add_constraints(arg1.get_byte(j) == known[j])


	sm = proj.factory.simulation_manager(ent_state)

	print(sm.active[0].solver.eval(arg1, cast_to=bytes))

	sm.explore(find=find_condition, avoid=fail)
	known.append(sm.found[0].solver.eval(arg1.get_byte(i), cast_to = bytes))

s = sm.active[0]
print("Done!")
print(s.solver.eval(arg1,cast_to=bytes))

