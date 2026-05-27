def min_max(a):
    if len(a) == 0:
        return None
    vt_min = vt_max = 0
    gt_min = gt_max = a[0]
    for i in range(1, len(a)):
        if a[i] < gt_min:
            gt_min = a[i]
            vt_min = i
        elif a[i] > gt_max:
            gt_max = a[i]
            vt_max = i
    return gt_min, vt_min, gt_max, vt_max
