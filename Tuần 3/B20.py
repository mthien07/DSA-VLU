def count_swap_bubble_sort(a):
    def merged_count(l, r):
        iv_count = 0
        i = j = 0
        merged_list = []
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                merged_list.append(l[i])
                i += 1
            else:
                merged_list.append(r[j])
                iv_count += (len(l) - i)
                j += 1
        merged_list.extend(l[i:])
        merged_list.extend(r[j:])
        return iv_count, merged_list