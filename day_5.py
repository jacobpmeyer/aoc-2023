from pprint import pprint

# This solution produces a number that is too high.
def seed_to_location(input):
    sections = input.split("\n")
    mappings = {}

    # Map the sections to a Python dictionary
    i = 0
    while i < len(sections) - 1:
        if sections[i] == "":
            i += 1
            j = i + 1
            section = sections[i].split(":")[0]
            while j < len(sections) and sections[j] != "":
                j += 1
            mappings[section] = sections[i+1:j]
            i = j

    # Split the seeds string and convert to int

    mappings["seeds"] = mappings["seeds"][0].split(" ")
    new_seeds = []
    for t in range(0, len(mappings["seeds"]), 2):
        first_num = int(mappings["seeds"][t])
        last_num = int(mappings["seeds"][t]) + int(mappings["seeds"][t+1])
        new_seeds.extend([u for u in range(first_num, last_num)])
    mappings["seeds"] = new_seeds

    # Add source and destination ranges
    for section, mapping in mappings.items():
        if section == "seeds":
            continue
        destination = []
        source = []
        for m in mapping:
            m = m.split(" ")
            destination.append([int(m[0]), int(m[0]) + int(m[2]) - 1])
            source.append([int(m[1]), int(m[1]) + int(m[2]) - 1])
        mappings[section] = {
            "destination": destination,
            "source": source
        }


    return min(run_seed(mappings["seeds"], mappings))


def run_seed(seeds, mappings):
    path = [
        "seed-to-soil map",
        "soil-to-fertilizer map",
        "fertilizer-to-water map",
        "water-to-light map",
        "light-to-temperature map",
        "temperature-to-humidity map",
        "humidity-to-location map"
    ]
    humidity_locations = []

    # lowest_range = []
    # lowest_idx = None
    # lowest_humidity = [float('inf'), float('inf')]
    # for pair in path["humidity-to-location map"]:
    #     if pair[0] < lowest_humidity[0]:
    #         lowest_humidity = pair

    # for step in reversed(path):
    #     if step == "humidity-to-location map":
    #         continue

    for seed_num in seeds:
        seed = int(seed_num)
        for step in path:
            source_list = mappings[step]["source"]
            destination_list = mappings[step]["destination"]
            for i in range(len(source_list)):
                if seed >= source_list[i][0] and seed <= source_list[i][1]:
                    seed = destination_list[i][0] + (seed - source_list[i][0])
                    break
        humidity_locations.append(seed)

    return humidity_locations

input1 = """
seeds:
79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

input2 = """
seeds:
194657215 187012821 1093203236 6077151 44187305 148722449 2959577030 152281079 3400626717 198691716 1333399202 287624830 2657325069 35258407 1913289352 410917164 1005856673 850939 839895010 162018909

seed-to-soil map:
466206721 134904099 264145987
3226739510 2500159633 122177414
1107118949 4139510909 155456387
2314679916 2622337047 59899451
2642618541 1908002826 511067679
0 399050086 167531444
1262575336 2682236498 1052104580
3448620320 1415756771 259155097
302435543 566581530 163771178
3348916924 4039807513 99703396
3153686220 1674911868 73053290
3788293662 1747965158 160037668
3948331330 3734341078 305466435
2374579367 1228806725 186950046
2561529413 2419070505 81089128
167531444 0 134904099
3707775417 1148288480 80518245
4253797765 1107118949 41169531

soil-to-fertilizer map:
3913658055 3217667557 44136240
3043638173 1755409772 387575354
1214033686 3261803797 213545970
3431213527 3475349767 482444528
1994011339 2522356968 695310589
2689321928 1214033686 354316245
1427579656 2142985126 379371842
1806951498 1568349931 187059841

fertilizer-to-water map:
2553394045 2097964132 64191777
3153687517 3499502814 665965431
1104565830 789107360 151317021
4084493704 2165934452 60088979
981078109 1551802916 123487721
2935219151 4165468245 66838136
10669639 1277616562 132965227
839228347 1410581789 141221127
3942173186 2018304529 79659603
393057134 444333135 344145590
2617585822 2253442971 317633329
4237573988 3156387517 57393308
1341340213 99436946 344896189
143634866 1746717555 204406814
776848617 0 21473714
386359019 1270918447 6698115
4168968434 3430897260 68605554
2497629182 3375132397 55764863
3819652948 3213780825 9721342
1686236402 940424381 47687418
4021832789 4232306381 62660915
4144582683 2162155909 3778543
1733923820 1675290637 30520902
737202724 21473714 39645893
2018304529 2591683508 479324653
798322331 1705811539 40906016
0 1260248808 10669639
980449474 788478725 628635
3002057287 3223502167 151630230
3829374290 2226023431 27419540
348041680 61119607 38317339
3856793830 3071008161 85379356
1764444722 1073569161 186679647
4148361226 2571076300 20607208
1255882851 988111799 85457362

water-to-light map:
3143216572 2396957585 46085818
2930160319 3087666064 82806318
3012966637 3275730008 11481558
1791164654 628261856 251676187
1156959152 1008045214 174725983
3597974089 4238330323 56636973
2659665097 3287211566 62612544
489714994 0 304501033
2323644539 2017991146 71374674
2611713237 3480351863 47951860
4135255968 3931716786 159711328
1331685135 879938043 128107171
2396957585 2748883399 70018348
408833803 1297158141 80881191
1469631779 1182771197 103330914
4004728215 3349824110 58812180
1012078485 2008335392 9655754
3024448195 2932857654 118768377
192304632 2089365820 87451432
4063540395 3408636290 71715573
3823753472 2665304126 83579273
117236420 1933267180 75068212
2218325460 1378039332 105319079
2722277641 3170472382 32223106
1459792306 618379493 9839473
3225342423 3528303723 55360789
901528396 304501033 110507199
3654611062 2471800766 96107890
1012035595 628218966 42890
1118925110 1719748519 38034042
3907332745 2567908656 97395470
2466975933 3786979482 144737304
794216027 1612436150 107312369
2901402956 2443043403 28757363
0 415008232 117236420
3750718952 3202695488 73034520
3189302390 3051626031 36040033
3394659119 3583664512 203314970
2754500747 4091428114 146902209
2042840841 1757782561 175484619
3280703212 2818901747 113955907
1021734239 532244652 86134841
279756064 1483358411 129077739
1572962693 2176817252 218201961
1107869080 1286102111 11056030

light-to-temperature map:
1609050489 2309171782 372577802
2023682469 2836643763 897111138
834447570 143604042 411534753
428779503 1217157762 28824561
143604042 931982301 108906615
252510657 1040888916 176268846
3431278062 1484221851 471209429
1981628291 3733754901 42054178
4140073117 2681749584 154894179
1484221851 4170138658 124828638
3902487491 1955431280 237585626
457604064 555138795 376843506
3036948483 3775809079 394329579
2920793607 2193016906 116154876

temperature-to-humidity map:
1348484361 0 45849582
1394333943 726347262 166590764
1797084784 3346946555 119105515
1163891565 1265639794 165909682
2199751891 3274125222 72821333
4012454029 2231107899 181228118
1008425725 207338839 56688993
2322219090 3174539335 24543729
3987057737 3199083064 25396292
1560924707 45849582 62712410
3424140824 1837299459 190417072
2272573224 3224479356 27702302
2346762819 2412336017 518856401
329181964 1432789749 172164254
3783666369 2027716531 203391368
753484930 471406467 254940795
1916190299 2931192418 243346917
501346218 892938026 44760077
1329801247 1604954003 18683114
2865619220 3567337219 558521604
546106295 264027832 207378635
2300275526 3252181658 21943564
4193682147 3466052070 101285149
327941691 1431549476 1240273
0 937698103 327941691
2159537216 1797084784 40214675
3614557896 4125858823 169108473
1065114718 108561992 98776847

humidity-to-location map:
440744287 1133551978 536306564
4042633851 4000620330 37465866
977050851 1669858542 136276424
2136551597 4038086196 256881100
198620952 0 242123335
1113327275 242123335 891428643
4080099717 3802748040 197872290
2695699324 2136551597 1346934527
4277972007 3785752751 16995289
2393432697 3483486124 302266627
0 1806134966 198620952
"""

print(seed_to_location(input1))
