inp = """departure location: 27-374 or 395-974
departure station: 40-287 or 295-953
departure platform: 27-554 or 570-961
departure track: 40-604 or 618-958
departure date: 43-842 or 850-972
departure time: 30-302 or 315-952
arrival location: 32-478 or 496-950
arrival station: 48-733 or 755-969
arrival platform: 37-260 or 276-954
arrival track: 40-512 or 519-964
class: 34-277 or 284-966
duration: 25-648 or 672-961
price: 28-684 or 705-956
route: 30-157 or 176-950
row: 47-881 or 903-970
seat: 38-705 or 727-959
train: 40-195 or 217-961
type: 28-858 or 879-958
wagon: 31-543 or 554-967
zone: 49-790 or 816-953

your ticket:
103,79,61,97,109,67,89,83,59,53,139,131,101,113,149,127,71,73,107,137

nearby tickets:
473,926,599,474,412,65,885,833,533,780,539,222,177,762,132,583,414,450,177,113
110,74,420,522,243,130,575,115,553,92,157,193,370,949,334,74,53,462,837,822
769,341,505,146,841,238,53,8,360,684,510,302,180,766,477,422,145,353,134,635
163,575,850,89,241,604,337,346,428,407,826,573,904,779,543,576,910,469,621,368
118,129,123,316,640,336,634,80,817,358,910,626,372,631,403,781,875,929,341,231
80,635,123,331,842,243,179,407,639,727,923,831,78,786,621,358,323,873,903,338
179,225,842,331,907,498,244,512,648,917,132,435,440,595,330,454,137,425,988,543
182,69,122,413,833,126,915,195,130,731,533,770,455,983,851,457,89,625,519,153
396,944,322,294,74,880,221,767,433,248,76,331,625,824,396,333,676,521,344,445
301,409,430,625,864,247,188,401,770,783,537,54,631,359,624,765,591,72,525,356
727,186,100,618,136,838,52,404,364,90,365,596,833,857,877,926,344,855,542,236
232,537,829,645,591,91,296,529,111,906,638,505,294,915,453,772,478,525,113,428
364,449,580,102,236,679,208,276,633,919,532,403,77,428,772,634,596,395,764,936
302,400,597,218,506,179,151,316,774,121,673,537,234,982,137,401,360,189,763,789
626,238,789,864,331,932,181,927,225,352,128,627,295,602,822,755,907,644,640,80
525,286,342,248,523,525,253,84,450,236,597,78,993,301,928,62,176,461,191,431
781,77,637,684,242,399,451,453,205,879,345,570,599,117,244,348,674,330,622,63
928,755,179,63,624,120,223,157,289,784,177,98,337,504,571,185,436,850,511,234
344,345,724,727,369,839,241,218,88,592,427,86,537,470,368,841,645,328,761,476
257,473,473,363,777,72,136,524,684,180,819,677,775,129,237,727,54,4,70,538
345,98,189,922,428,351,641,256,946,60,835,333,925,578,543,930,333,622,223,4
726,535,415,96,296,908,919,460,398,462,233,767,229,245,913,54,620,323,602,783
905,351,769,587,178,449,124,154,329,518,584,731,115,369,469,52,907,452,833,143
343,845,773,585,820,398,828,853,287,858,444,778,935,422,766,257,76,521,831,678
253,279,367,599,462,334,220,137,245,853,576,627,363,360,333,853,677,188,51,835
821,654,730,180,937,421,459,732,157,448,368,470,497,439,756,604,646,93,327,193
768,341,223,190,581,929,544,777,628,349,284,457,506,903,106,156,457,89,182,536
980,182,915,633,316,93,627,522,146,588,680,94,583,915,224,156,916,530,457,932
537,325,638,905,624,940,610,931,477,51,770,324,469,146,922,789,177,299,340,576
532,790,538,219,774,622,324,361,223,319,420,115,607,777,923,57,761,836,820,98
81,831,417,947,906,546,635,125,771,497,287,76,73,645,147,776,579,258,53,453
80,225,470,337,340,503,69,324,144,194,778,905,848,235,247,364,932,756,110,258
287,710,943,473,156,910,237,318,143,786,347,469,181,369,57,230,121,426,60,929
500,765,301,778,191,427,442,880,537,838,593,759,729,848,474,932,527,407,684,576
585,639,104,856,582,627,603,456,363,246,231,762,514,142,353,348,355,453,755,819
926,778,823,538,581,343,402,834,422,530,464,705,308,397,497,533,539,188,585,435
105,521,932,499,250,573,844,353,932,295,903,95,192,944,340,351,777,930,674,336
779,142,852,727,473,590,269,945,923,942,542,674,95,676,195,446,432,328,114,250
76,842,157,131,133,328,437,523,903,109,638,340,104,240,911,277,761,601,872,327
418,557,836,907,147,854,855,910,92,924,251,328,395,477,125,114,818,326,932,907
917,146,222,339,825,464,326,243,606,910,764,181,65,178,940,299,276,223,683,832
638,537,589,490,433,819,249,126,352,396,681,154,788,239,596,105,357,591,121,832
932,346,585,552,618,118,787,826,152,786,219,250,58,672,647,531,907,255,534,640
374,299,244,181,645,260,869,504,772,66,329,768,120,287,401,624,140,414,851,620
239,355,91,600,134,730,246,460,598,521,705,827,911,129,536,343,361,840,502,16
321,291,928,769,50,224,64,346,228,446,431,109,437,880,680,334,301,317,908,399
936,259,148,513,75,519,318,525,936,222,466,639,67,583,770,705,407,906,346,323
325,585,250,256,820,23,589,120,318,322,855,576,767,826,635,434,852,193,180,104
675,456,248,730,444,328,13,543,879,451,345,405,286,534,881,592,184,106,771,256
371,632,228,597,852,255,98,330,679,219,602,920,914,299,233,249,417,111,270,536
373,533,331,580,637,651,100,285,415,841,948,942,430,405,351,64,143,300,620,410
51,239,239,782,916,235,425,138,512,341,454,999,908,941,142,531,755,852,931,193
251,142,573,779,253,94,226,903,595,455,271,850,591,54,427,107,631,826,344,602
628,945,218,441,466,141,821,762,156,56,922,50,296,498,436,912,260,487,463,86
588,79,761,70,841,347,449,520,249,789,127,134,405,904,454,271,496,233,834,53
784,850,106,68,841,92,931,285,326,68,182,731,446,516,406,644,441,420,223,823
249,322,587,903,502,942,231,467,235,948,292,818,497,857,533,476,822,68,575,526
87,319,339,423,352,224,74,222,134,790,411,625,227,337,87,987,531,628,920,325
364,541,646,74,185,453,187,838,10,507,915,781,626,587,632,763,772,625,621,405
474,823,442,332,510,132,457,372,236,489,576,372,523,921,576,58,759,821,588,345
369,371,514,334,149,316,136,584,774,776,123,912,462,128,944,362,447,429,732,119
345,65,362,529,787,232,351,153,110,400,762,912,497,258,352,431,817,632,993,81
430,259,917,121,109,574,571,857,257,470,939,354,455,712,948,582,764,400,315,826
831,422,818,104,581,827,246,410,251,857,501,910,496,865,823,915,217,647,415,221
769,416,536,673,346,509,596,944,284,365,620,12,596,943,471,335,767,102,536,370
502,519,362,129,946,640,69,181,440,457,486,756,914,244,470,229,504,361,296,790
933,597,251,70,191,97,125,88,150,126,516,773,642,243,832,323,832,103,194,82
250,217,783,252,125,421,430,61,647,133,278,525,185,436,147,154,450,645,326,84
353,106,426,143,445,340,347,415,637,506,250,453,494,572,778,191,420,113,929,336
818,941,519,830,406,132,102,916,105,536,923,778,359,456,406,228,522,787,400,483
397,451,455,337,59,250,125,435,834,183,243,410,154,908,1,425,463,363,226,397
316,787,399,645,373,471,586,111,501,241,456,364,117,372,905,515,948,184,819,66
278,755,837,821,407,496,358,342,470,511,675,327,318,80,321,455,400,672,152,83
55,529,931,925,587,677,825,240,667,594,431,530,618,245,335,498,230,850,729,453
316,242,762,141,473,246,783,397,117,239,837,51,530,438,976,765,932,435,331,419
451,547,187,458,154,401,531,675,62,403,231,533,104,755,98,919,406,944,520,122
288,339,922,822,180,414,646,524,50,523,597,423,418,299,500,248,459,145,842,318
194,785,547,130,789,619,324,347,60,543,89,401,57,322,917,401,78,505,528,54
434,455,130,763,645,512,294,926,432,674,355,97,927,554,231,620,497,155,319,594
95,130,944,726,122,947,941,192,538,728,77,676,193,121,328,352,354,81,186,880
353,816,355,219,570,141,761,156,62,224,189,253,195,18,73,100,906,778,318,619
481,533,411,112,934,759,856,580,276,438,622,233,880,540,681,620,362,527,780,727
625,779,297,604,880,436,186,949,220,761,392,241,857,762,251,914,941,468,370,226
561,676,780,254,598,829,397,147,594,727,176,321,96,598,335,783,599,584,836,881
106,543,881,184,418,731,298,18,150,184,853,730,56,576,132,766,915,346,441,637
502,147,647,786,251,106,835,397,467,337,912,940,219,544,836,594,924,429,182,583
821,626,841,464,247,785,147,462,21,128,186,238,238,65,781,604,929,228,678,241
465,188,98,322,81,474,255,634,562,141,498,254,347,94,225,928,858,463,407,915
634,540,642,400,357,526,171,397,574,455,178,684,246,579,364,324,82,941,767,365
419,462,358,177,367,277,186,131,633,623,502,357,911,906,981,439,903,532,402,907
851,774,994,75,760,181,816,70,944,589,233,938,359,54,149,236,828,529,220,679
414,230,785,450,779,586,836,628,907,185,597,923,368,585,851,505,232,994,258,772
326,432,853,935,445,775,781,224,760,858,612,636,521,89,347,357,323,413,577,602
226,340,227,378,400,528,534,598,912,510,93,588,786,109,907,469,456,453,842,82
74,62,223,322,925,186,411,838,51,788,258,594,429,281,408,841,463,366,577,644
269,190,433,284,75,729,927,366,142,239,766,427,853,233,929,347,646,934,142,287
155,784,319,858,71,503,672,777,638,826,365,758,835,329,929,490,118,113,531,496
786,108,907,524,78,87,451,836,846,239,822,74,472,445,67,776,925,519,584,369
943,593,619,445,831,373,55,75,537,581,701,72,500,925,462,371,823,107,91,932
620,222,880,917,217,514,432,364,910,243,354,731,111,472,286,97,125,755,947,850
855,576,912,116,409,424,392,818,223,542,592,857,323,913,543,349,630,930,684,925
923,590,632,576,473,567,436,757,220,930,348,779,438,362,519,919,100,593,498,786
845,217,414,774,933,318,73,648,830,108,542,347,51,337,365,156,131,903,816,543
894,759,525,908,436,130,287,829,879,71,98,447,684,554,426,595,583,786,295,510
921,348,818,925,124,270,905,533,97,348,227,250,919,84,918,154,538,773,645,588
590,938,943,554,631,139,697,411,604,339,537,822,319,67,519,176,247,116,936,189
540,923,128,620,497,362,512,218,852,636,835,63,91,432,56,998,179,155,347,188
69,435,112,776,627,825,63,324,681,542,372,141,931,999,398,453,636,256,462,771
129,939,531,189,903,504,903,104,631,596,774,147,697,626,781,527,677,935,276,820
583,590,944,462,485,768,775,586,182,336,648,779,727,476,126,523,95,83,767,141
583,378,945,633,150,780,454,948,63,643,366,344,534,146,639,134,452,356,50,142
945,225,194,827,542,938,217,512,926,315,705,24,942,441,59,903,242,927,402,477
831,395,916,195,595,772,761,444,599,622,724,588,407,647,455,116,245,475,938,819
340,529,670,154,339,408,834,90,512,339,61,185,333,588,915,428,508,575,932,413
588,54,150,417,767,418,90,191,403,572,369,132,224,457,143,789,459,505,468,262
395,285,906,221,296,424,55,354,598,771,439,371,548,633,113,539,635,424,398,432
757,398,82,636,835,107,507,144,761,259,730,857,568,354,672,572,857,153,106,355
521,918,849,73,90,641,134,913,97,82,341,447,771,576,770,857,499,241,505,928
944,151,522,991,241,778,259,537,403,913,760,133,366,858,81,441,374,538,426,831
314,477,57,103,107,178,935,529,633,442,618,940,447,61,543,824,128,177,625,447
527,71,537,219,352,401,771,484,114,402,573,68,326,525,284,251,837,286,407,604
300,149,504,572,672,937,146,228,150,441,337,231,944,542,66,529,588,441,479,184
391,64,642,536,362,234,646,68,577,916,526,914,761,501,191,63,461,348,370,856
112,625,235,565,109,458,935,113,856,70,134,255,118,539,360,77,935,224,128,783
937,456,6,362,91,462,768,932,543,103,766,140,56,406,790,153,585,464,128,780
458,403,928,616,594,646,176,780,818,459,87,732,354,146,231,677,258,528,300,904
414,948,180,757,522,576,66,69,311,182,593,56,342,822,436,144,632,838,945,445
782,80,589,506,647,848,628,644,395,405,180,790,419,498,841,248,257,323,63,439
119,681,410,182,132,787,119,622,362,107,764,472,51,453,436,824,227,838,817,977
946,729,62,757,328,921,396,733,147,344,550,915,763,111,880,58,680,134,229,58
146,127,398,948,266,597,451,880,783,817,235,937,106,420,762,352,420,830,87,630
317,81,574,638,922,185,326,498,448,730,52,110,335,618,498,456,246,399,478,7
771,903,77,363,255,183,642,82,131,506,477,153,392,354,224,413,416,128,683,461
66,928,420,245,915,597,777,619,53,190,476,408,540,348,514,576,144,445,839,836
242,84,274,322,374,585,54,783,769,678,128,82,276,64,329,78,591,333,337,829
225,539,593,130,643,334,283,931,396,123,80,785,928,851,106,315,276,359,904,344
414,629,774,127,407,325,402,338,819,276,637,505,788,610,237,140,133,521,135,227
51,65,542,183,512,69,601,582,403,90,314,103,90,111,856,505,590,914,618,333
94,317,408,347,832,592,504,148,410,764,589,252,604,95,91,509,406,99,501,670
414,538,442,765,345,571,458,530,759,623,58,367,627,459,464,933,761,590,112,551
541,858,229,407,934,817,181,678,373,181,422,53,240,61,287,52,944,219,75,518
469,421,537,283,519,620,602,330,75,135,341,358,644,346,577,593,499,355,512,462
299,527,461,225,368,256,188,250,408,684,978,781,256,51,85,916,463,301,302,534
94,781,765,106,92,475,98,371,446,248,788,984,156,911,154,438,679,591,919,780
870,332,840,590,97,328,122,467,759,336,924,452,930,405,347,683,851,532,826,448
352,257,783,930,324,918,470,125,516,341,399,408,591,683,771,179,627,733,187,357
638,299,6,467,639,235,136,732,349,286,764,645,619,855,362,176,733,430,604,55
995,788,471,242,434,229,779,295,142,455,322,597,851,287,520,534,324,63,462,839
199,647,68,452,252,374,783,824,446,682,372,912,330,419,573,195,248,176,442,107
54,86,372,423,829,774,328,590,450,575,858,635,996,259,75,466,250,108,730,854
501,577,788,60,146,852,458,497,779,817,919,91,667,353,462,632,352,758,914,903
300,949,416,624,645,624,915,434,296,226,622,784,762,931,764,642,332,195,2,640
553,220,913,727,442,926,366,416,357,473,426,53,59,728,61,917,230,478,504,504
122,51,292,422,828,81,276,511,52,833,534,587,587,629,414,911,644,408,357,646
53,592,817,927,371,398,346,331,254,420,401,761,538,90,466,668,90,506,523,908
834,336,625,767,932,943,220,683,228,504,528,942,283,128,349,647,942,604,192,90
857,681,573,327,2,913,858,360,832,403,130,347,183,648,929,785,904,942,594,672
589,438,822,763,454,182,591,281,352,841,235,69,841,236,537,123,790,644,422,104
529,778,759,276,301,122,127,411,478,51,671,153,645,157,433,410,340,622,640,919
131,277,316,302,139,629,437,629,455,649,777,137,320,728,468,192,464,330,841,323
587,939,450,767,905,789,319,851,729,424,684,842,72,454,759,731,1,591,88,768
765,506,932,303,355,190,227,67,147,604,629,238,948,245,598,254,528,411,187,590
3,446,472,497,365,374,331,130,65,232,778,237,619,500,880,941,728,345,176,783
945,93,146,138,68,344,277,906,193,374,846,229,140,575,411,63,91,584,836,834
917,836,136,499,329,910,357,74,450,786,208,674,939,57,326,148,106,86,238,498
436,480,369,618,428,831,287,348,756,823,69,833,177,93,243,328,93,913,673,528
635,535,439,337,465,574,115,537,879,779,236,911,648,509,102,819,975,733,519,69
769,345,759,339,833,824,543,833,638,84,941,508,267,356,424,135,530,250,131,499
327,138,54,684,905,246,126,357,287,88,787,775,352,152,337,722,426,784,122,512
64,634,103,622,343,240,64,249,226,852,980,601,73,497,469,182,190,153,853,444
367,431,527,319,634,349,572,355,769,818,598,501,423,660,829,358,679,459,581,119
193,59,414,853,231,447,285,98,105,399,625,906,221,683,580,498,585,755,185,707
782,824,832,243,253,297,440,116,130,192,129,829,766,941,75,291,842,462,369,399
246,430,858,90,641,872,770,424,939,243,323,939,635,914,624,760,299,370,925,463
703,244,772,782,432,469,435,522,429,769,317,133,521,464,460,915,92,531,906,684
823,341,351,122,79,784,301,270,790,347,574,758,597,260,588,457,87,910,423,594
515,832,732,246,299,573,644,920,510,186,61,71,68,325,528,371,443,543,94,784
226,682,572,587,502,593,61,297,274,420,89,827,457,571,936,122,764,519,447,635
629,316,98,60,98,717,462,641,832,72,426,296,86,632,775,580,775,412,62,329
217,932,59,102,61,252,910,400,584,602,871,229,823,179,787,120,191,341,78,57
137,124,83,644,440,765,223,468,227,822,86,769,260,218,316,440,151,120,67,862
142,542,452,62,639,839,56,411,872,940,248,330,903,240,114,137,570,236,447,570
133,477,878,188,89,680,182,157,119,471,775,839,54,523,832,626,57,511,326,435
940,852,929,238,431,679,757,651,256,90,855,584,189,239,177,760,235,419,554,819
118,927,780,228,370,596,627,923,598,320,330,354,868,467,243,919,457,247,397,116
837,462,120,138,130,604,345,417,943,132,107,287,851,81,494,519,632,116,113,102
86,437,424,246,932,131,926,398,945,721,218,779,540,581,816,768,836,301,185,402
117,633,327,99,640,532,679,221,143,783,781,529,215,683,593,419,132,372,622,531
537,496,941,586,835,279,348,912,498,537,353,538,254,345,295,642,145,683,103,628
92,880,503,841,412,597,941,188,355,89,774,934,634,512,909,996,102,910,730,429
678,56,191,180,134,74,630,523,828,395,411,643,434,453,247,788,597,15,416,56
618,90,679,467,361,943,509,862,330,926,645,596,398,122,818,138,522,946,128,76
509,577,728,66,918,504,586,349,540,532,512,822,420,932,275,409,948,181,944,301
83,613,369,403,218,253,764,761,147,365,156,817,631,295,502,823,541,451,183,682
619,344,79,423,298,521,773,335,775,225,259,755,851,291,239,235,542,582,776,909
468,850,110,407,652,598,836,733,460,757,783,254,400,822,554,55,100,592,76,589
73,143,357,834,581,188,667,456,374,591,534,466,302,780,425,506,466,102,908,298
781,300,527,936,470,418,495,117,85,374,241,909,362,727,238,140,457,926,648,65
359,824,947,94,108,486,91,570,427,238,461,779,135,578,727,71,191,679,255,277
322,944,98,150,50,587,177,60,641,638,602,921,367,266,184,786,239,593,833,156
433,76,983,620,573,449,776,89,633,330,500,941,185,603,125,76,645,337,790,256
639,539,412,127,449,674,505,239,419,626,427,252,91,494,89,852,919,842,463,77
340,414,366,542,585,442,304,622,504,128,928,949,904,400,414,588,110,578,822,535
940,57,344,594,524,464,456,675,137,471,445,625,527,247,257,279,629,439,500,346
500,409,66,249,398,76,932,120,722,327,631,673,473,147,767,116,321,512,763,144
641,284,260,947,635,767,908,507,394,237,940,441,102,183,919,195,936,435,95,368
614,234,398,77,331,841,132,243,319,781,621,349,335,302,108,133,152,635,360,765
603,329,629,64,108,220,504,78,279,425,254,932,247,355,353,357,728,370,819,105
453,453,362,328,786,123,516,87,255,433,520,634,780,536,424,257,52,573,528,501
787,275,935,529,539,185,915,828,498,348,916,578,576,463,445,634,191,188,152,140
438,585,471,192,138,408,125,65,254,460,820,319,923,398,93,881,19,629,240,942
57,460,234,622,286,600,808,416,786,856,345,121,705,731,768,449,926,135,324,436
589,497,125,54,592,183,828,573,233,270,519,907,133,145,373,352,619,580,74,346
629,241,114,258,423,114,433,520,254,917,626,448,638,979,587,301,448,618,462,914
446,634,149,103,249,67,596,836,276,190,573,399,17,477,628,50,784,155,943,229
509,599,355,660,634,638,446,571,402,593,357,134,81,404,233,395,125,765,104,346
138,904,87,532,920,467,717,425,442,233,730,104,338,185,836,61,504,357,143,73
777,759,322,252,374,289,58,580,344,82,79,879,705,227,536,57,302,401,922,729
54,397,437,823,469,447,371,466,581,253,559,318,587,497,822,531,331,342,941,928
120,409,320,633,834,757,123,260,419,642,945,181,159,918,526,358,256,67,673,285
320,506,176,261,508,149,325,105,430,618,829,189,924,783,772,522,584,923,521,369
468,518,936,521,76,286,534,816,123,234,914,402,502,829,596,841,571,65,470,501
348,925,526,150,936,157,765,912,763,432,316,331,459,755,655,151,72,593,672,444
727,638,397,682,337,401,497,629,284,278,147,360,672,230,779,187,136,595,365,619
239,78,469,623,142,122,579,131,554,417,629,404,915,564,362,511,233,247,451,497
768,474,96,501,364,151,584,405,995,248,728,636,498,374,340,766,436,420,641,827
625,775,785,581,621,412,507,622,403,570,71,446,716,347,295,57,534,244,630,246
467,83,280,367,522,246,630,431,330,239,928,220,181,604,95,67,120,154,578,904
58,878,947,501,411,440,922,912,938,434,765,526,418,916,931,113,921,906,104,769
683,502,241,120,337,419,621,517,228,286,97,119,364,575,119,156,149,252,478,76
670,374,423,543,236,109,927,358,632,347,368,248,787,477,100,149,921,728,943,231
229,832,395,397,411,224,368,770,530,864,223,949,258,445,535,682,624,322,589,947
142,936,683,347,537,276,362,106,596,227,428,591,147,477,637,598,233,298,276,279
933,597,572,402,66,104,528,942,493,102,177,137,148,421,639,454,684,179,824,779
134,336,180,499,113,592,19,583,125,445,534,128,81,502,463,346,941,836,257,497
458,332,923,851,539,903,569,948,925,919,105,257,760,677,296,438,465,511,932,621
404,185,487,285,249,223,827,435,80,77,406,468,451,92,354,342,124,95,786,191
684,520,357,127,679,779,241,259,89,410,767,524,474,442,731,551,542,837,255,96
675,297,591,116,150,927,365,464,931,241,502,84,59,625,295,299,359,55,996,629
287,538,856,845,111,464,227,676,254,576,420,366,325,507,402,57,535,117,59,906
681,87,351,54,939,77,318,433,440,52,505,443,371,931,231,867,574,148,939,137"""