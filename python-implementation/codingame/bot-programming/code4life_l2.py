import sys
import math

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!


project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

game_loop = 1
working_mode = 0
# working mode
# 0 start
# 1 at SAMPLES
# 2 done collecting samples
# 3 at DIAGNOSIS
# 4 done for dignos sample data
# 5 at MOLECULES
# 6 done for collecting MOLECULES
# 7 at LABORATORY
# 8 done for submiting samples and molecules
# game loop
while True:
    print("game_loop:{}".format(game_loop), file=sys.stderr)

    targets = []
    storages = []

    for i in range(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        storage = {}
        targets.append(target)
        eta = int(eta)
        score = int(score)
        storage['a'] = int(storage_a)
        storage['b'] = int(storage_b)
        storage['c'] = int(storage_c)
        storage['d'] = int(storage_d)
        storage['e'] = int(storage_e)
        storages.append(storage)
        
        expertise_a = int(expertise_a)
        expertise_b = int(expertise_b)
        expertise_c = int(expertise_c)
        expertise_d = int(expertise_d)
        expertise_e = int(expertise_e)
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]

    sample_count = int(input())
    samples = {}
    high_value_ids = []

    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()

        sample = {}
        sample_data = {}

        sample_data['carried_by'] = int(carried_by)
        sample_data['rank'] = int(rank)
        sample_data['experties_gain'] = int(expertise_gain)
        sample_data['health'] = int(health)
        sample_data['cost'] = {}
        sample_data['cost']['a'] = int(cost_a)
        sample_data['cost']['b'] = int(cost_b)
        sample_data['cost']['c'] = int(cost_c)
        sample_data['cost']['d'] = int(cost_d)
        sample_data['cost']['e'] = int(cost_e)
        samples[sample_id] = sample_data

    print("samples:{}".format(samples), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages..."    , file=sys.stderr)
    print("target:{}".format(targets[0]), file=sys.stderr)
    print("working mode:{}".format(working_mode), file=sys.stderr)
    game_loop += 1

    if targets[0] == 'START_POS' or working_mode == 8:
        print("====1====", file=sys.stderr)
        print("GOTO SAMPLES")
        working_mode = 1
        continue

    if targets[0] == 'SAMPLES' and working_mode == 1:
        print("====2====", file=sys.stderr)
        rank = 2
        print("CONNECT {}".format(rank))
        working_mode = 2
        continue
    
    if targets[0] == 'SAMPLES' or working_mode == 2:
        print("====3====", file=sys.stderr)
        print("GOTO DIAGNOSIS")
        working_mode = 3
        continue
    
    if targets[0] == 'DIAGNOSIS' and working_mode == 3:
        print("====4====", file=sys.stderr)
        for current_id in samples.keys():
            working_sample = samples[current_id]
            if working_sample['carried_by'] == 0:
                break

        working_sample_id = current_id
        print("sample_id:{}, carried_by:{}".format(working_sample_id, working_sample['carried_by']), file=sys.stderr)
        print("CONNECT {}".format(working_sample_id))
        working_mode = 4
        continue

    if working_mode == 4:
        print("====5====", file=sys.stderr)
        print("GOTO MOLECULES")
        working_mode = 5
        continue
        
    if working_mode == 5:
        working_sample = samples[working_sample_id]
        print("working sample{}".format(working_sample), file=sys.stderr)
        count = 0
        print("storage:{}".format(storages[0]), file=sys.stderr)
        print("needed:{}".format(working_sample['cost']), file=sys.stderr)
        for molecule, needed in working_sample['cost'].items():
            print("getting {}: needed:{}, storage:{}".format(molecule, needed, storages[0][molecule]), file=sys.stderr)
            if storages[0][molecule] < needed:
                print("====5====", file=sys.stderr)
                print("CONNECT {}".format(molecule.upper()))
                break
            else:
                count += 1
        print("count:{}".format(count), file=sys.stderr)
        if count == 5:
            print("GOTO LABORATORY")
            working_mode = 7
            continue

    if working_mode == 7:
        print("working sample id:{}".format(working_sample_id), file=sys.stderr)
        print("====8====", file=sys.stderr)
        print("CONNECT {}".format(working_sample_id))
        working_mode = 8
        continue
