def toh(steps,disc_count, source_rod, destination_rod, placeholder_rod):
    """towers of hanoi recursive algorithm"""
    if disc_count == 1:
        #print("Move disc 1 from rod",source_rod,"to rod",destination_rod)
        steps.append((1,source_rod,destination_rod))
        return
    toh(steps,disc_count-1, source_rod, placeholder_rod, destination_rod)
    #print("Move disc",discCount,"from rod",source_rod,"to rod",destination_rod)
    steps.append((disc_count,source_rod,destination_rod))
    toh(steps,disc_count-1, placeholder_rod, destination_rod, source_rod)