# https://www.codingame.com/ide/puzzle/code4life
import sys


def print_debug(text):
    print(text, file=sys.stderr)


def cost_minus_cost(cost1, cost2):
    cost = {key: cost1.get(key, 0) - cost2.get(key, 0) for key in set(cost1) | set(cost2)}
    return dict(sorted(cost.items()))


def cost_add_cost(cost1, cost2):
    cost = {key: cost1.get(key, 0) + cost2.get(key, 0) for key in set(cost1) | set(cost2)}
    return dict(sorted(cost.items()))


def remove_zero_cost(cost):
    none_zero_cost = {x: y for x, y in cost.items() if y != 0}
    return none_zero_cost


def replace_neg_cost_with_zero(cost):
    for x, y in cost.items():
        if y < 0:
            cost[x] = 0
    return dict(sorted(cost.items()))


def list_minus_list(list1, list2):
    for value in list2:
        list1.remove(value)
    return list1


def sort_dict_by_value(dict1, reverse=True):
    return dict(sorted(dict1.items(), key=lambda x: x[1], reverse=reverse))


def get_distance(start, end):
    index_matrix = {
        'START_POS': 0,
        'SAMPLES': 1,
        'DIAGNOSIS': 2,
        'MOLECULES': 3,
        'LABORATORY': 4
    }

    start_i = index_matrix[start]
    end_i = index_matrix[end]
    distance_matrix = [
        [0, 2, 2, 2, 2],
        [0, 3, 3, 3, 3],
        [0, 3, 0, 3, 4],
        [0, 3, 3, 0, 3],
        [0, 3, 4, 3, 0]
    ]
    return distance_matrix[start_i][end_i]


def is_sample_diagnosed(s):
    if s['health'] != -1:
        return True
    return False


def dead_lock_samples_id(his_samples, my_expertise, my_storage, molecule_left, all_samples):
    dead_lock_sample_list = []
    if len(his_samples) == 0:
        for sample_id, sample_data in all_samples.items():
            if sample_data['carried_by'] != 1:
                for molecule, cost in sample_data['cost'].items():
                    my_needs = cost - my_expertise[molecule] - my_storage[molecule]
                    if my_needs > molecule_left[molecule]:
                        dead_lock_sample_list.append(sample_id)
        print_debug('dead_lock_samples:{}'.format(dead_lock_sample_list))
    return dead_lock_sample_list


def ready_to_submit_molecule(his_samples, his_storage, his_expertise, all_samples):
    total_ready_to_submit_molecule = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    storage_left = his_storage.copy()
    for sample_id in his_samples:
        print_debug('checking sample:{}'.format(sample_id))
        submit_molecule = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
        tmp_storage = storage_left.copy()
        gain = all_samples[sample_id]['expertise_gain'].lower()
        print_debug('gain:{}'.format(gain))
        count = 0
        for molecule, cost in all_samples[sample_id]['cost'].items():
            print_debug('{}:cost:{},exp:{},store_left:{}'.format(molecule, cost, his_expertise[molecule],
                                                                 storage_left[molecule]))
            need = cost - his_expertise[molecule] if cost > 0 else 0
            if storage_left[molecule] >= need:
                submit_molecule[molecule] = need if need > 0 else 0
                tmp_storage[molecule] -= submit_molecule[molecule]
                count += 1
        if count == 5:
            print_debug('his sample:{},submit_molecule:{}'.format(sample_id, submit_molecule))
            storage_left = tmp_storage
            if gain != '0':
                storage_left[gain] += 1
            total_ready_to_submit_molecule = cost_add_cost(submit_molecule, total_ready_to_submit_molecule)
    print_debug('total_ready_to_submit:{}'.format(total_ready_to_submit_molecule))


def undiagnosed_samples_id(samples_id, allsamples):
    undiagnosed_samples = []
    for sample_id in samples_id:
        if not is_sample_diagnosed(allsamples[sample_id]):
            undiagnosed_samples.append(sample_id)
    # print_debug('undiagnosed samples id:{}'.format(undiagnosed_samples))
    return undiagnosed_samples


def sample_ranks(samples_id, allsamples):
    samples_rank = []
    for sample_id in samples_id:
        samples_rank.append(allsamples[sample_id]['rank'])
    print_debug('sample ranks:{}'.format(samples_rank))
    return samples_rank


def sample_expertise_gain(samples_id, allsamples):
    samples_exp_gain = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for sample_id in samples_id:
        gain = allsamples[sample_id]['expertise_gain'].lower()
        if gain != '0':
            samples_exp_gain[gain] += 1
    # print_debug('samples_exp_gain:{}'.format(samples_exp_gain))
    return samples_exp_gain


def all_current_needs(my_samples, his_samples, my_submit_samples, my_expertise, his_expertise, my_storage, his_storage,
                      allsamples):
    my_samples_cost = get_total_molecule_needs(my_samples, allsamples)
    his_samples_cost = get_total_molecule_needs(his_samples, allsamples)

    my_current_needs = cost_minus_cost(my_samples_cost, my_expertise)
    my_current_needs = cost_minus_cost(my_current_needs, my_storage)
    his_current_needs = cost_minus_cost(his_samples_cost, his_expertise)
    his_current_needs = cost_minus_cost(his_current_needs, his_storage)
    my_exp_gain = sample_expertise_gain(my_samples, allsamples)
    his_exp_gain = sample_expertise_gain(his_samples, allsamples)

    # print_debug('available:  {}'.format(available))
    # print_debug('my_cost:    {}'.format(my_samples_cost))
    # print_debug('my_exp:     {}'.format(my_expertise))
    # print_debug('my_storage: {}'.format(my_storage))
    # print_debug('my_needs:   {}'.format(my_current_needs))
    # print_debug('my_exp_gain:{}'.format(my_exp_gain))

    if my_submit_samples:
        for sample_id in my_submit_samples:
            gain = allsamples[sample_id]['expertise_gain'].lower()
            my_current_needs[gain] -= 1

    # print_debug('his_cost:    {}'.format(his_samples_cost))
    # print_debug('his_exp:     {}'.format(his_expertise))
    # print_debug('his_storage: {}'.format(my_storage))
    # print_debug('his_needs:   {}'.format(his_current_needs))
    # print_debug('his_exp_gain:{}'.format(his_exp_gain))

    my_current_needs = remove_zero_cost(replace_neg_cost_with_zero(my_current_needs))
    his_current_needs = remove_zero_cost(replace_neg_cost_with_zero(his_current_needs))

    return my_current_needs, his_current_needs


def get_min_common_needs(my_expertise, my_storage, my_samples_id, allsamples):
    min_common_needs = {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}
    for sample_id in my_samples_id:
        costs = allsamples[sample_id]['cost']
        gain = allsamples[sample_id]['expertise_gain']
        print_debug('{}:costs:{}:gain:{}'.format(sample_id, costs, gain))
        my_current_needs = cost_minus_cost(costs, my_expertise)
        my_current_needs = cost_minus_cost(my_current_needs, my_storage)
        # print_debug('{}:my_current_needs:{}'.format(sample_id,my_current_needs))
        for molecule, cost in my_current_needs.items():
            if cost < min_common_needs[molecule]:
                min_common_needs[molecule] = cost if cost >= 0 else 0
    # print_debug('   min_common_needs:{}'.format(min_common_needs))
    return min_common_needs


def is_expertise_enough_for_my_sample(my_expertise, sample_id, allsamples):
    # print_debug('validating sample:{}'.format(sample))
    molecule_limit = 10
    max_molecule = 5
    for molecule, cost in allsamples[sample_id]['cost'].items():
        # print_debug("checking {}: needed({}), myexp({}), available({})"
        # .format(molecule, needed, myexpertise[molecule], available[molecule]))
        molecule_limit = molecule_limit - (cost - my_expertise[molecule])
        if cost > (max_molecule + my_expertise[molecule]):
            print_debug("sample:{} {}:cost({}) > exp({}) + {}".format(sample_id, molecule, cost, my_expertise[molecule],
                                                                      max_molecule))
            return False
        if molecule_limit < 0:
            print_debug("sample:{} {}:cost({}) + exp({}) > {}".format(sample_id, molecule, cost, my_expertise[molecule],
                                                                      molecule_limit))
            return False
    return True


def cloud_samples_id(allsamples):
    cloud_samples = []
    for sample_id in allsamples.keys():
        if allsamples[sample_id]['carried_by'] == -1:
            cloud_samples.append(sample_id)
    print_debug('cloud samples id:{}'.format(cloud_samples))
    return cloud_samples


def his_samples_id(allsamples):
    his_samples = []
    for sample_id in allsamples.keys():
        if allsamples[sample_id]['carried_by'] == 1:
            his_samples.append(sample_id)
    # print_debug('his samples id:{}'.format(his_samples))
    return his_samples


def validated_samples_id(expertises, sample_ids, allsamples):
    validated_samples = []
    my_expertise = expertises[0]
    for sample_id in sample_ids:
        # print_debug('validating sample:{}'.format(sample_id))
        is_my_expertise_enough = is_expertise_enough_for_my_sample(my_expertise, sample_id, allsamples)
        is_max_molecule_enough = True

        if not is_sample_diagnosed(allsamples[sample_id]):
            continue
        if is_my_expertise_enough and is_max_molecule_enough and allsamples[sample_id]['expertise_gain'] != 0:
            validated_samples.append(sample_id)
    # print_debug('validated samples id:{}'.format(validated_samples))
    return validated_samples


def get_total_molecule_needs(samples_id, allsamples):
    total_melecule_needs = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for sample_id in samples_id:
        # print_debug('checking submit:{}'.format(sample_id))
        for molecule, cost in allsamples[sample_id]['cost'].items():
            if cost > 0:
                total_melecule_needs[molecule] += cost
    return total_melecule_needs


def ready_for_lab_samples_id(myexpertise, mystorage, samples_id, allsamples):
    submit_samples_id = []
    storage_left = mystorage.copy()
    for sample_id in samples_id:
        # print_debug('checking submit:{}'.format(sample_id))
        # print_debug('storage({})'.format(mystorage))
        # print_debug('costs({})'.format(allsamples[sample_id]['cost'].items()))
        gain = allsamples[sample_id]['expertise_gain'].lower()
        if is_sample_diagnosed(allsamples[sample_id]):
            count = 0
            tmp_storage = storage_left.copy()
            for molecule, cost in allsamples[sample_id]['cost'].items():
                needs = cost - myexpertise[molecule]
                # print_debug("{},needs({}),exp({}),storage_left({})"\
                #    .format(molecule.upper(), needs, myexpertise[molecule],storage_left[molecule]))
                if needs <= storage_left[molecule]:
                    count += 1
                    if needs > 0:
                        tmp_storage[molecule] = tmp_storage[molecule] - needs
            # print_debug('count:{}'.format(count))
            if count == 5:
                submit_samples_id.append(sample_id)
                storage_left = tmp_storage
                storage_left[gain] += 1
    print_debug('submit samples id:{}'.format(submit_samples_id))
    # print_debug('storage left:{}'.format(storage_left))
    return submit_samples_id, storage_left


def best_sample_for_science_project(projects_needs, sample_candidates, myexpertise):
    best_samples = []
    if len(sample_candidates) > 1:
        smallest_needs = nearest_science_project_gap(projects_needs, myexpertise)
        for sample_id in sample_candidates:
            if samples[sample_id]['expertise_gain'].lower() in list(smallest_needs.keys()):
                best_samples.append(sample_id)
    print_debug('best samples:{}'.format(best_samples))
    return best_samples


def nearest_science_project_gap(projects, myexpertise):
    smallest_needs = {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}
    for project_need in projects:
        # print_debug('project needs:{}'.format(project_need))
        # print_debug('myexpertise  :{}'.format(myexpertise))
        gaps = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
        for molecule, needs in project_need.items():
            gap = needs - myexpertise[molecule]
            if gap > 0:
                gaps[molecule] = gap
        if sum(gaps.values()) < sum(smallest_needs.values()):
            smallest_needs = gaps
    # print_debug('smallest project gap:{}'.format(smallest_needs))
    smallest_needs_copy = remove_zero_cost(smallest_needs)
    print_debug('smallest project gap:{}'.format(smallest_needs_copy))
    return smallest_needs_copy


def cal_best_rank(available_storage, my_expertise, my_samples, undiagnosed_samples):
    not_completed_samples = len(my_samples) - len(undiagnosed_samples)
    rank = 1
    if sum(my_expertise.values()) > 10 and available_storage > 4 and not_completed_samples < 1:
        rank = 3
    elif sum(my_expertise.values()) > 5 and available_storage > 1 and not_completed_samples < 2:
        rank = 2
    return rank


def sort_samples_by_health(samples_id, allsamples):
    sample_health_mapping = {}
    for sample_id in samples_id:
        health = allsamples[sample_id]['health']
        sample_health_mapping[sample_id] = health
    print_debug('sample_health:{}'.format(sample_health_mapping))
    sorted_samples = [k for k in sorted(sample_health_mapping, key=sample_health_mapping.get, reverse=True)]
    print_debug('sorted_samples_by_health:{}'.format(sorted_samples))
    return sorted_samples


def sort_samples_by_cost(samples_id, my_expertise, allsamples):
    sample_needs_score = {}
    sample_needs_mapping = {}
    all_needs = {}
    for sample_id in samples_id:
        costs = allsamples[sample_id]['cost']
        total_need = cost_minus_cost(costs, my_expertise)
        total_need = replace_neg_cost_with_zero(total_need)
        sample_needs_mapping[sample_id] = total_need
        sample_needs_score[sample_id] = sum(total_need.values())
        all_needs = cost_add_cost(all_needs, total_need)

    print_debug('sample_needs_mapping:{}'.format(sample_needs_mapping))
    print_debug('sample_needs_score:{}'.format(sample_needs_score))
    print_debug('all_needs:{}'.format(all_needs))

    for sample_id, total_need in sample_needs_mapping.items():
        gain = samples[sample_id]['expertise_gain'].lower()
        others_needs = remove_zero_cost(cost_minus_cost(all_needs, total_need))
        # print_debug('gain:{}'.format(gain))
        # print_debug('others_needs:{}'.format(others_needs))
        if gain in list(others_needs.keys()):
            sample_needs_score[sample_id] -= 1

    print_debug('sample_needs_score:{}'.format(sample_needs_score))
    sorted_samples = [k for k in sorted(sample_needs_score, key=sample_needs_score.get, reverse=False)]
    print_debug('sorted_samples_by_needs_score:{}'.format(sorted_samples))
    return sorted_samples


def continue_collect_samples(available, my_samples, my_expertise, my_storage, allsamples):
    enough_samples = []
    # print_debug('available:{}'.format(available))
    # print_debug('my_storage:{}'.format(my_storage))
    all_have = cost_add_cost(available, my_storage)
    print_debug('all_have:{}'.format(all_have))
    for sample_id in my_samples:
        cost = allsamples[sample_id]['cost']
        print_debug('cost:{}'.format(cost))
        gain = allsamples[sample_id]['expertise_gain'].lower()
        need = cost_minus_cost(cost, my_expertise)
        print_debug('need:{}'.format(need))
        need = replace_neg_cost_with_zero(need)

        rest_molecule = cost_minus_cost(all_have, need)
        print_debug('sample:{}, rest_molecule:{}'.format(sample_id, rest_molecule))
        count = 0
        for molecule, value in rest_molecule.items():
            if value < 0:
                print_debug('{} not enough for sample:{}'.format(molecule, sample_id))
                break
            else:
                count += 1
        if count == 5:
            print_debug('sample {} can continue to collect'.format(sample_id))
            enough_samples.append(sample_id)
            all_have = rest_molecule
            all_have[gain] += 1
    return enough_samples


def cal_best_molecule(sorted_my_samples, submit_samples, storage_left, available, my_expertise, his_current_needs,
                      allsamples):
    # min_common_needs = get_min_common_needs(my_expertise, storage_left, my_samples, available, allsamples)
    # min_common_needs = remove_zero_cost(min_common_needs)
    # print_debug('min_common_needs:{}'.format(min_common_needs))
    # if list(min_common_needs.keys()):
    #    molecule = list(min_common_needs.keys())[0]
    # if available[molecule] != 0:
    #     return molecule

    # collect by sorted samples first, not enough molecule samples put to break_samples
    collecting_samples = list_minus_list(sorted_my_samples.copy(), submit_samples)
    sorted_available_molecule = [k for k, v in sorted(available.items(), key=lambda x: x[1], reverse=False)]

    break_samples = []
    for working_sample_id in collecting_samples:
        working_sample = allsamples[working_sample_id]
        print_debug("working sample id: {}".format(working_sample_id))
        switch_sample = False
        for molecule in sorted_available_molecule:
            cost = working_sample['cost'][molecule]
            needs = cost - storage_left[molecule] - my_expertise[molecule]
            print_debug("getting {}:needs:{},cost:{},storage_left:{},exp:{},available:{}"
                        .format(molecule.upper(), needs, cost, storage_left[molecule], my_expertise[molecule],
                                available[molecule]))
            if available[molecule] == 0 and needs > 0:
                switch_sample = True
                break_samples.append(working_sample_id)
                break
            if available[molecule] != 0 and needs > 0:
                return molecule
        if switch_sample:
            continue

    # continue break samples to collect
    if break_samples:
        for working_sample_id in break_samples:
            working_sample = allsamples[working_sample_id]
            print_debug("break sample:{}".format(working_sample_id))
            for molecule in sorted_available_molecule:
                cost = working_sample['cost'][molecule]
                needs = cost - storage_left[molecule] - my_expertise[molecule]
                print_debug("getting {}:needs:{},cost:{},storage_left:{},exp:{},available:{}"
                            .format(molecule.upper(), cost, storage_left[molecule], my_expertise[molecule], needs,
                                    available[molecule]))
                if available[molecule] != 0 and needs > 0:
                    return molecule

    # start to collect his needs to prevent
    if his_current_needs:
        sorted_his_current_needs_key = [k for k, v in
                                        sorted(his_current_needs.items(), key=lambda x: x[1], reverse=True)]
        molecule = sorted_his_current_needs_key[0]
        if available[molecule] != 0:
            print_debug('working on his needs:{}'.format(sorted_his_current_needs_key))
            return molecule

    return 0


project_count = int(input())
projects_needs = []
for i in range(project_count):
    needs_value = [int(j) for j in input().split()]
    needs_key = ['a', 'b', 'c', 'd', 'e']
    needs = dict(zip(needs_key, needs_value))
    projects_needs.append(needs)

print_debug("projects_needs:{}".format(projects_needs))

game_loop = 0
# game loop
while True:
    # Contains both players, 0 is myself
    targets = []
    etas = []
    scores = []
    storages = []
    expertises = []

    # Contains data used for both player
    available = {}
    samples = {}
    my_samples = []

    for i in range(2):
        target, eta, score, sto_a, sto_b, sto_c, sto_d, sto_e, exp_a, exp_b, exp_c, exp_d, exp_e = input().split()
        storage = {'a': int(sto_a), 'b': int(sto_b), 'c': int(sto_c), 'd': int(sto_d), 'e': int(sto_e)}
        expertise = {'a': int(exp_a), 'b': int(exp_b), 'c': int(exp_c), 'd': int(exp_d), 'e': int(exp_e)}
        targets.append(target)
        etas.append(int(eta))
        scores.append(int(score))
        storages.append(storage)
        expertises.append(expertise)

    available['a'], available['b'], available['c'], available['d'], available['e'] = [int(i) for i in input().split()]
    sample_count = int(input())

    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        cost = {'a': int(cost_a), 'b': int(cost_b), 'c': int(cost_c), 'd': int(cost_d), 'e': int(cost_e)}
        sample_data = {'carried_by': int(carried_by), 'rank': int(rank), 'expertise_gain': expertise_gain,
                       'health': int(health), 'cost': cost}
        samples[sample_id] = sample_data

        if int(carried_by) == 0:
            my_samples.append(sample_id)

    game_loop += 1
    print_debug("game_loop:{}".format(game_loop))
    print_debug('---my---')
    his_samples = his_samples_id(samples)
    sorted_my_samples = sort_samples_by_cost(my_samples, expertises[0], samples)
    cloud_samples = cloud_samples_id(samples)
    valid_cloud_samples = validated_samples_id(expertises, cloud_samples, samples)
    undiagnosed_samples = undiagnosed_samples_id(sorted_my_samples, samples)
    validated_samples = validated_samples_id(expertises, sorted_my_samples, samples)
    submit_samples, storage_left = ready_for_lab_samples_id(expertises[0], storages[0], sorted_my_samples, samples)
    get_min_common_needs(expertises[0], storages[0], sorted_my_samples, samples)
    my_current_needs, his_current_needs = all_current_needs(sorted_my_samples, his_samples, submit_samples,
                                                            expertises[0], expertises[1], storages[0], storages[1],
                                                            samples)
    dead_lock_samples = dead_lock_samples_id(his_samples, expertises[0], storages[0], available, samples)
    available_storage = 10 - sum(storages[0].values())
    # print_debug('available_storage:{}'.format(available_storage))
    # print_debug("my targets:{}".format(targets[0]))
    # print_debug("my eta:{}".format(etas[0]))
    print_debug("valid_cloud_samples:{}".format(valid_cloud_samples))
    # print_debug("my samples:{}".format(my_samples))
    print_debug('all_current_needs:{}'.format(my_current_needs))

    print_debug('---his---')
    print_debug('all_current_needs:{}'.format(his_current_needs))

    print_debug('====================')

    if etas[0] > 0:
        print("GOTO EMPTY")
        continue

    if targets[0] == 'START_POS':
        print("GOTO SAMPLES")
        continue

    if targets[0] == 'SAMPLES':
        rank = cal_best_rank(available_storage, expertises[0], my_samples, undiagnosed_samples)
        if len(my_samples) == 3:
            print("GOTO DIAGNOSIS")
        else:
            print("CONNECT {}".format(rank))
        continue

    if targets[0] == 'DIAGNOSIS':
        # Diagnose all samples
        if len(undiagnosed_samples) != 0:
            print("CONNECT {}".format(undiagnosed_samples.pop()))
            continue
        # Deadlock samples
        if len(dead_lock_samples) != 0:
            sample_ids = [i for i in my_samples if i in dead_lock_samples]
            if sample_ids:
                print("CONNECT {}".format(sample_ids.pop()))
                continue
        # Handle storage is full situation
        if available_storage == 0:
            if len(submit_samples) != 0:
                print('GOTO LABORATORY')
            elif len(my_samples) > 0:
                print("CONNECT {}".format(my_samples.pop()))
            else:
                print('GOTO SAMPLES')
            continue

        # send invalid samples back to cloud
        store_to_cloud_samples = [i for i in my_samples if i not in validated_samples]
        # calculate best samples between my_samples and valid_cloud_samples
        download_from_cloud_samples = []
        best_samples = []
        if len(valid_cloud_samples) != 0:
            # avoid the dead_lock samples to download back
            for sample_id in dead_lock_samples:
                if sample_id not in best_samples and sample_id in valid_cloud_samples:
                    valid_cloud_samples.remove(sample_id)

            sample_candidates = valid_cloud_samples + my_samples
            print_debug('sample_candidates:{}'.format(sample_candidates))
            best_samples = best_sample_for_science_project(projects_needs, sample_candidates, expertises[0])

            best_sample_inhand = [i for i in best_samples if i in my_samples]
            best_sample_not_inhand = [i for i in best_samples if i not in my_samples]
            best_sample_not_inhand = sort_samples_by_health(best_sample_not_inhand, samples)

            not_best_sample_inhand = [i for i in my_samples if i not in best_samples]
            not_best_sample_not_inhand = [i for i in valid_cloud_samples if i not in best_samples]
            not_best_sample_not_inhand = sort_samples_by_health(not_best_sample_not_inhand, samples)

            # Download all samples
            if len(sample_candidates) <= 3:
                download_from_cloud_samples = valid_cloud_samples
            # only download best sample not inhand
            elif len(best_sample_not_inhand) + len(my_samples) <= 3:
                download_from_cloud_samples = best_sample_not_inhand
                capacity_in_hand = 3 - len(best_sample_not_inhand) - len(my_samples)
                if capacity_in_hand > 0:
                    download_from_cloud_samples += not_best_sample_not_inhand[:capacity_in_hand]
            # exchange the samples
            elif (len(best_sample_not_inhand) + len(my_samples)) > 3 and len(best_sample_inhand) != 3:
                capacity_in_hand = 3 - len(best_sample_inhand)
                if len(best_sample_not_inhand) < capacity_in_hand:
                    download_from_cloud_samples = best_sample_not_inhand
                else:
                    download_from_cloud_count = capacity_in_hand
                    download_from_cloud_samples = best_sample_not_inhand[:download_from_cloud_count]
                    store_to_cloud_samples = not_best_sample_inhand

        print_debug('store_to_cloud:{}'.format(store_to_cloud_samples))
        print_debug('download_from_cloud:{}'.format(download_from_cloud_samples))

        # store samples back to cloud
        if len(store_to_cloud_samples) != 0:
            print("CONNECT {}".format(store_to_cloud_samples.pop()))
            continue
        # download samples from cloud
        if len(download_from_cloud_samples) != 0 and len(my_samples) < 3:
            print("CONNECT {}".format(download_from_cloud_samples.pop()))
            continue
        # collect samples again if only 1 sample in hand
        if len(my_samples) < 2:
            print('GOTO SAMPLES')
            continue

    if targets[0] == 'MOLECULES':
        if (200 - game_loop) == (3 + len(submit_samples)):
            print('GOTO LABORATORY')
            continue

        if len(dead_lock_samples) == 3:
            print('GOTO DIAGNOSIS')
            continue

        if available_storage == 0:
            print_debug('10 molecule storage limit reached!')
            if len(submit_samples) != 0:
                print('GOTO LABORATORY')
            elif len(my_samples) != 3 and len(valid_cloud_samples) == 0:
                print('GOTO SAMPLES')
            else:
                print('GOTO DIAGNOSIS')
            continue

        molecule_tobe_collect = cal_best_molecule(sorted_my_samples, submit_samples, storage_left, available,
                                                  expertises[0], his_current_needs, samples)

        if molecule_tobe_collect != 0:
            print('CONNECT {}'.format(molecule_tobe_collect))
            continue
        else:
            if len(submit_samples) > 0:
                print("GOTO LABORATORY")
                continue
            if len(my_samples) < 3:
                if len(valid_cloud_samples) != 0:
                    print('GOTO DIAGNOSIS')
                else:
                    print('GOTO SAMPLES')
                continue
            else:
                print("WAIT")
                continue

    if targets[0] == 'LABORATORY':
        if len(submit_samples) != 0:
            print("CONNECT {}".format(submit_samples.pop(0)))
            continue
        if len(my_samples) != 0:
            continue_samples = continue_collect_samples(available, my_samples, expertises[0], storages[0], samples)
            if len(continue_samples) == 0:
                if len(valid_cloud_samples) != 0:
                    print('GOTO DIAGNOSIS')
                else:
                    print('GOTO SAMPLES')
                continue
            elif available_storage != 0:
                print('GOTO MOLECULES')
                continue

    if targets[0] != 'SAMPLES' and len(my_samples) == 0:
        print_debug("====1====")
        print("GOTO SAMPLES")
        continue

    if targets[0] != 'DIAGNOSIS' and (len(undiagnosed_samples) != 0 and len(my_samples) == len(undiagnosed_samples)):
        print_debug("====2====")
        print("GOTO DIAGNOSIS")
        continue

    if targets[0] != 'MOLECULES' and available_storage != 0 and len(my_samples) > 0 \
            and len(undiagnosed_samples) == 0 and len(validated_samples) == len(my_samples):
        print_debug("====3====")
        print("GOTO MOLECULES")
        continue

    if targets[0] != 'LABORATORY' and len(submit_samples) != 0 and len(submit_samples) == len(my_samples):
        print_debug("====4====")
        print("GOTO LABORATORY")
        continue

    if available_storage == 0:
        if len(my_samples) != 3 and len(valid_cloud_samples) == 0:
            print('GOTO SAMPLES')
        else:
            print('GOTO DIAGNOSIS')
