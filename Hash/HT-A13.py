def day_lien_tiep_dai_nhat(mang):
    tap_hop = set(mang)
    max_dai = 0
    
    for so in tap_hop:
        if so - 1 not in tap_hop:
            hien_tai = so
            do_dai = 1
            while hien_tai + 1 in tap_hop:
                hien_tai += 1
                do_dai += 1
            max_dai = max(max_dai, do_dai)
            
    return max_dai

mang = [100, 4, 200, 1, 3, 2]
print(f"Day lien tiep dai nhat trong {mang} co do dai:", day_lien_tiep_dai_nhat(mang))
