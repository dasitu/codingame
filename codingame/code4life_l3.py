import sys
import math

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

def print_debug(text):
    print(text, file=sys.stderr)
    
def get_distance(start, end):
    index_matrx = {
        'START_POS' : 0,
        'SAMPLES'   : 1,
        'DIAGNOSIS' : 2,
        'MOLECULES' : 3,
        'LABORATORY': 4
    }

    start_i = index_matrx[start]
    end_i = index_matrx[end]
    distance_matrix = [
        [0,2,2,2,2],
        [0,3,3,3,3],
        [0,3,0,3,4],
        [0,3,3,0,3],
        [0,3,4,3,0]
    ]
    return distance_matrix[start_i][end_i]

def is_sample_diagnosed(sample):
    if sample['health'] != -1:
        return True
    return False

def undiagnosed_sample_count(samples):
    undiagnosed_count = 0
    for sample_id in samples.keys():
        if not is_sample_diagnosed(samples[sample_id]):
            undiagnosed_count += 1
    print_debug('my undiagnosed sample count:{}'.format(undiagnosed_count))
    return undiagnosed_count

def is_expertise_enough_for_my_sample(myexpertise, sample):
    #print_debug('validing sample:{}'.format(sample))
    molecule_limit = 10
    max_molecule = 5
    for molecule, needed in sample['cost'].items():
        print_debug("checking {}: needed({}), myexp({}), available({})".format(molecule, needed, myexpertise[molecule], available[molecule]))
        molecule_limit = molecule_limit - (needed - myexpertise[molecule])
        if needed > (max_molecule + myexpertise[molecule]):
            print_debug("needed({}) > exp({}) + {}".format(needed, myexpertise[molecule],max_molecule))
            return False
            break
        if molecule_limit < 0:
            print_debug("needed({}) + exp({}) > {}".format(needed, myexpertise[molecule],molecule_limit))
            return False
            break
    return True

def get_validated_sample_count(myexpertise, samples):
    validated_count = 0
    for sample_id in samples.keys():
        print_debug('validating sample:{}'.format(sample_id))
        if is_expertise_enough_for_my_sample(myexpertise, samples[sample_id]):
            validated_count += 1
    print_debug('validated_count:{}'.format(validated_count))
    return validated_count
    
    
def ready_for_lab_sample_id(myexpertise, storages, samples):
    for sample_id in samples.keys():
        print_debug('submit id:{}?'.format(sample_id))
        count = 0
        for molecule, needed in samples[sample_id]['cost'].items():
            if needed <= myexpertise[molecule] + storages[molecule] and needed != -1:
                print_debug("{},needed({}),exp({}),storage({})".format(molecule.upper(), needed, myexpertise[molecule],storages[molecule]))
                count += 1
        print_debug('count:{}'.format(count))
        if count == 5:
            print_debug('ready_for_submit_sample_id:{}'.format(sample_id))
            return sample_id
    return -1

project_count = int(input())
projects_needs = []
for i in range(project_count):
    needs_value = [int(j) for j in input().split()]
    needs_key = ['a','b','c','d','e']
    needs = dict(zip(needs_key, needs_value))
    projects_needs.append(needs)

print_debug("projects_needs:{}".format(projects_needs))


game_loop = 1
# game loop
while True:
    print_debug("game_loop:{}".format(game_loop))
    
    
    # Contains both players, 0 is myself
    targets = []
    etas = []
    scores = []
    storages = []
    expertises = []
    
    # Contains data used for both player
    available = {}
    samples = {}
    mysamples = {}
    
    for i in range(2):
        storage = {}
        expertise = {}
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        targets.append(target)
        etas.append(int(eta))
        scores.append(int(score))
        storage['a'] = int(storage_a)
        storage['b'] = int(storage_b)
        storage['c'] = int(storage_c)
        storage['d'] = int(storage_d)
        storage['e'] = int(storage_e)
        storages.append(storage)
        
        expertise['a'] = int(expertise_a)
        expertise['b'] = int(expertise_b)
        expertise['c'] = int(expertise_c)
        expertise['d'] = int(expertise_d)
        expertise['e'] = int(expertise_e)
        expertises.append(expertise)
        
    available['a'], available['b'], available['c'], available['d'], available['e'] = [int(i) for i in input().split()]
    sample_count = int(input())

    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample = {}
        sample_data = {}
        sample_data['carried_by'] = int(carried_by)
        sample_data['rank'] = int(rank)
        sample_data['experties_gain'] = expertise_gain
        sample_data['health'] = int(health)
        sample_data['cost'] = {}
        sample_data['cost']['a'] = int(cost_a)
        sample_data['cost']['b'] = int(cost_b)
        sample_data['cost']['c'] = int(cost_c)
        sample_data['cost']['d'] = int(cost_d)
        sample_data['cost']['e'] = int(cost_e)
        samples[sample_id] = sample_data
        
        if int(carried_by) == 0:
            mysamples[sample_id] = sample_data

    my_undiagnosed_sample_count = undiagnosed_sample_count(mysamples)
    validated_sample_count = get_validated_sample_count(expertises[0], mysamples)
    submit_sample_id = ready_for_lab_sample_id(expertises[0], storages[0], mysamples)
    
    print_debug("my targets:{}".format(targets[0]))
    print_debug("my eta:{}".format(etas[0]))
    print_debug("my expertise:{}".format(expertises[0]))
    #print_debug("all samples:{}".format(samples))
    print_debug("my samples:{}".format(mysamples))

    
    if etas[0] > 0:
        print("WAIT")
        continue
    
    if targets[0] == 'START_POS' or (targets[0] != 'SAMPLES' and len(mysamples) == 0):
        print_debug("====1====")
        print("GOTO SAMPLES")
        continue

    if targets[0] != 'DIAGNOSIS' and my_undiagnosed_sample_count != 0 and len(mysamples) == 3:
        print_debug("====2====")
        print("GOTO DIAGNOSIS")
        continue
    
    if targets[0] != 'MOLECULES' and len(mysamples) != 0 and my_undiagnosed_sample_count == 0 and submit_sample_id == -1 and validated_sample_count == len(mysamples):
        print_debug("====3====")
        print("GOTO MOLECULES")
        continue
    
    if targets[0] != 'LABORATORY' and submit_sample_id != -1:
        print_debug("====4====")
        print_debug('ready to submit_id:{}'.format(submit_sample_id))
        print("GOTO LABORATORY")
        continue
    
    if targets[0] == 'SAMPLES' and len(mysamples) < 3:
        print_debug("====5====")
        rank = 2
        if sum(expertises[0].values()) > 5:
            rank = 3
        print_debug("rank:{}".format(rank))
        print("CONNECT {}".format(rank))
        continue
    
    if targets[0] == 'DIAGNOSIS' and (my_undiagnosed_sample_count != 0 or validated_sample_count < len(mysamples)):
        print_debug("====6====")
        for current_id in mysamples.keys():
            print_debug('Diagnosing sample id:{}'.format(current_id))
            working_sample = samples[current_id]
            working_sample_id = current_id
            if is_sample_diagnosed(working_sample):
                if not is_expertise_enough_for_my_sample(expertises[0], working_sample):
                    print_debug('send back to cloud:{}'.format(working_sample_id))
                    print("CONNECT {}".format(working_sample_id))
                    break
            else:
                print_debug('Diagnose ID:{}'.format(working_sample_id))
                print("CONNECT {}".format(working_sample_id))
                break
        continue
    
    if targets[0] == 'MOLECULES':
        print_debug("====7====")
        for current_id in mysamples.keys():
            working_sample = samples[current_id]
            working_sample_id = current_id
            print_debug("working sample id {}".format(working_sample_id))
            for molecule, needed in working_sample['cost'].items():
                inner_loop_break = False
                switch_sample = False
                print_debug("getting {}: needed:{}, storage:{}, exp:{}, available:{}".format(molecule.upper(), needed, storages[0][molecule], expertises[0][molecule], available[molecule]))
                if available[molecule] == 0 and (storages[0][molecule] + expertises[0][molecule]) < needed:
                    print_debug('+++++++++++++++++')
                    print("GOTO SAMPLES")
                    inner_loop_break = True
                    break
                if (storages[0][molecule] + expertises[0][molecule]) < needed:
                    print("CONNECT {}".format(molecule.upper()))
                    inner_loop_break = True
                    break
            if inner_loop_break:
                break

    if targets[0] == 'LABORATORY':
        print_debug("====8====")
        print("CONNECT {}".format(submit_sample_id))
        continue
    
    game_loop += 1