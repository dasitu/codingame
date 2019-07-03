import sys
import math

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!


project_count = int(raw_input())
for i in xrange(project_count):
    a, b, c, d, e = [int(j) for j in raw_input().split()]

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
    print >> sys.stderr, "game_loop:{}".format(game_loop)
    
    targets = []
    storages = []
    
    for i in xrange(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = raw_input().split()
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
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in raw_input().split()]
    

    sample_count = int(raw_input())
    samples = {}
    high_value_ids = []
    
    for i in xrange(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = raw_input().split()
        
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

    print >> sys.stderr, "samples:{}".format(samples)
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."    
    print >> sys.stderr, "target:{}".format(targets[0])
    print >> sys.stderr, "working mode:{}".format(working_mode)
    game_loop += 1
    
    if targets[0] == 'START_POS' or working_mode == 8:
        print >> sys.stderr, "====1===="
        print("GOTO SAMPLES")
        working_mode = 1
        continue
    
    if targets[0] == 'SAMPLES' and working_mode == 1:
        print >> sys.stderr, "====2===="
        rank = 2
        print("CONNECT {}".format(rank))
        working_mode = 2
        continue
    
    if targets[0] == 'SAMPLES' or working_mode == 2:
        print >> sys.stderr, "====3===="
        print("GOTO DIAGNOSIS")
        working_mode = 3
        continue
    
    if targets[0] == 'DIAGNOSIS' and working_mode == 3:
        print >> sys.stderr, "====4===="
        for current_id in samples.keys():
            working_sample = samples[current_id]
            if working_sample['carried_by'] == 0:
                break
        
        working_sample_id = current_id
        print >> sys.stderr, "sample_id:{}, carried_by:{}".format(working_sample_id, working_sample['carried_by'])
        print "CONNECT {}".format(working_sample_id)
        working_mode = 4
        continue
    
    if working_mode == 4:
        print >> sys.stderr, "====5===="
        print "GOTO MOLECULES"
        working_mode = 5
        continue
        
    if working_mode == 5:
        working_sample = samples[working_sample_id]
        print >> sys.stderr, "working sample{}".format(working_sample)
        count = 0
        print >> sys.stderr, "storage:{}".format(storages[0])
        print >> sys.stderr, "needed:{}".format(working_sample['cost'])
        for molecule, needed in working_sample['cost'].iteritems():
            print >> sys.stderr, "getting {}: needed:{}, storage:{}".format(molecule, needed, storages[0][molecule])
            if storages[0][molecule] < needed:
                print >> sys.stderr, "====5===="
                print "CONNECT {}".format(molecule.upper())
                break
            else:
                count += 1
        print >> sys.stderr, "count:{}".format(count)
        if count == 5:
            print "GOTO LABORATORY"
            working_mode = 7
            continue
        
    if working_mode == 7:
        print >> sys.stderr, "working sample id:{}".format(working_sample_id)
        print >> sys.stderr, "====8===="
        print "CONNECT {}".format(working_sample_id)
        working_mode = 8
        continue
