import array

bug_bmp = [
(1,0),(2,0),(3,0),(5,0),
(6,0),(7,0),(3,1),(4,1),
(5,1),(0,2),(2,2),(3,2),
(4,2),(5,2),(6,2),(8,2),
(0,3),(1,3),(2,3),(3,3),
(5,3),(6,3),(7,3),(8,3),
(2,4),(3,4),(5,4),(6,4),
(0,5),(1,5),(2,5),(3,5),
(5,5),(6,5),(7,5),(8,5),
(2,6),(3,6),(5,6),(6,6),
(0,7),(1,7),(2,7),(3,7),
(4,7),(5,7),(6,7),(7,7),
(8,7),(0,8),(8,8)
    ]

cat_1_l_bmp = [
(0,0),(1,1),(3,1),(4,1),
(1,2),(2,2),(3,2),(4,2),
(5,2),(1,3),(2,3),(3,3),
(4,3),(2,4),(3,4),(4,4),
(2,5),(3,5),(4,5),(2,6),
(3,6),(4,6),(2,7),(3,7),
(4,7),(2,8),(3,8),(4,8),
(2,9),(3,9),(4,9),(5,9),
(0,10),(1,10),(2,10),(3,10),
(5,10),(2,11),(5,11),(1,12),
(4,12),(3,13),(2,14)
    ]

cat_2_l_bmp = [
(3,0),(4,0),(3,1),(4,1),(3,2),
(4,2),(5,2),(0,3),(2,3),(3,3),
(0,4),(1,4),(2,4),(3,4),(4,4),
(0,5),(1,5),(2,5),(3,5),(4,5),
(1,6),(2,6),(3,6),(4,6),(2,7),
(3,7),(2,8),(3,8),(1,9),(2,9),
(1,10),(1,11),(2,11),(2,12),(2,13),
(3,13),(3,14)
    ]

cat_1_r_bmp = [
(5,0),(1,1),(2,1),(4,1),(0,2),
(1,2),(2,2),(3,2),(4,2),(1,3),
(2,3),(3,3),(4,3),(1,4),(2,4),
(3,4),(1,5),(2,5),(3,5),(1,6),
(2,6),(3,6),(1,7),(2,7),(3,7),
(1,8),(2,8),(3,8),(0,9),(1,9),
(2,9),(3,9),(0,10),(2,10),(3,10),
(4,10),(5,10),(0,11),(3,11),(1,12),
(4,12),(2,13),(3,14)
    ]

cat_2_r_bmp = [
(1,0),(2,0),(1,1),(2,1),(0,2),
(1,2),(2,2),(2,3),(3,3),(5,3),
(1,4),(2,4),(3,4),(4,4),(5,4),
(1,5),(2,5),(3,5),(4,5),(5,5),
(1,6),(2,6),(3,6),(4,6),(2,7),
(3,7),(2,8),(3,8),(3,9),(4,9),
(4,10),(3,11),(4,11),(3,12),(2,13),
(3,13),(2,14)
    ]

welcome_screen_x_bmp = array.array('I', [
0, 1, 5, 6, 10, 11, 13, 14, 16, 17, 24, 25, 30, 31, 32, 
33, 49, 50, 51, 52, 53, 0, 1, 5, 6, 10, 11, 13, 16, 17, 
24, 25, 28, 29, 30, 31, 32, 33, 34, 44, 45, 49, 50, 51, 52, 
53, 54, 1, 2, 5, 6, 7, 10, 11, 13, 14, 16, 17, 21, 22, 
23, 24, 25, 28, 29, 33, 34, 38, 39, 40, 43, 44, 45, 46, 49, 
50, 53, 54, 57, 58, 61, 62, 64, 65, 67, 68, 1, 2, 4, 5, 
6, 7, 9, 10, 13, 14, 16, 17, 20, 21, 22, 23, 24, 25, 28, 
29, 37, 38, 39, 40, 41, 43, 44, 45, 46, 49, 50, 53, 54, 57, 
58, 61, 62, 64, 65, 66, 67, 68, 69, 97, 121, 122, 1, 2, 4, 
5, 7, 9, 10, 13, 14, 16, 17, 20, 21, 24, 25, 28, 29, 37, 
38, 41, 44, 45, 49, 50, 51, 52, 53, 57, 58, 61, 62, 64, 65, 
68, 69, 97, 98, 99, 100, 119, 120, 121, 122, 2, 4, 7, 9, 10, 
13, 14, 16, 17, 20, 21, 24, 25, 28, 29, 37, 38, 39, 40, 41, 
44, 45, 49, 50, 52, 53, 57, 58, 61, 62, 64, 65, 68, 69, 97, 
98, 99, 100, 101, 102, 117, 118, 119, 120, 121, 2, 3, 4, 7, 8, 
9, 13, 14, 16, 17, 20, 21, 24, 25, 28, 29, 33, 34, 37, 38, 
41, 44, 45, 49, 50, 53, 54, 57, 58, 61, 62, 64, 65, 68, 69, 
97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 
112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 2, 3, 4, 7, 8, 
9, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 25, 28, 29, 30, 
31, 32, 33, 34, 37, 38, 40, 41, 44, 45, 46, 49, 50, 53, 54, 
57, 58, 59, 60, 61, 62, 64, 65, 68, 69, 97, 98, 99, 100, 101, 
102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 
117, 118, 119, 120, 121, 3, 4, 8, 9, 13, 14, 16, 17, 18, 21, 
22, 23, 24, 25, 30, 31, 32, 33, 37, 38, 39, 40, 41, 44, 45, 
46, 49, 50, 54, 57, 58, 59, 60, 61, 62, 64, 65, 68, 69, 97, 
98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
113, 114, 115, 116, 117, 118, 119, 120, 121, 97, 98, 99, 100, 101, 102, 
103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 
108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 97, 
98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
113, 114, 115, 116, 117, 118, 119, 120, 121, 97, 98, 99, 100, 101, 102, 
103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 
107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 
122, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 
110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 96, 97, 
98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 96, 97, 98, 99, 100, 
101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 
116, 117, 118, 119, 120, 121, 122, 1, 2, 3, 4, 5, 6, 25, 26, 
36, 37, 41, 42, 45, 46, 55, 56, 60, 61, 65, 66, 74, 75, 78, 
79, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 1, 
2, 5, 6, 7, 25, 26, 29, 36, 37, 41, 42, 49, 50, 55, 56, 
59, 60, 61, 64, 65, 74, 75, 78, 79, 92, 93, 95, 96, 97, 98, 
99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 
114, 115, 116, 117, 118, 119, 120, 121, 122, 125, 126, 1, 2, 6, 7, 
11, 12, 13, 14, 17, 18, 20, 21, 22, 25, 26, 28, 29, 30, 31, 
36, 37, 41, 42, 45, 46, 48, 49, 50, 51, 55, 56, 59, 60, 61, 
64, 65, 68, 69, 70, 74, 75, 78, 79, 82, 83, 84, 85, 94, 95, 
96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 
1, 2, 6, 7, 10, 11, 14, 15, 17, 18, 19, 21, 22, 25, 29, 
30, 36, 37, 38, 39, 40, 41, 42, 45, 46, 48, 49, 50, 51, 56, 
57, 59, 61, 62, 64, 65, 67, 68, 69, 70, 71, 74, 75, 78, 79, 
81, 82, 85, 86, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 
107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 
122, 1, 2, 6, 7, 10, 11, 14, 15, 17, 18, 21, 22, 29, 30, 
36, 37, 38, 39, 40, 41, 42, 45, 46, 49, 50, 56, 57, 59, 61, 
62, 64, 71, 74, 75, 78, 79, 82, 83, 96, 97, 98, 99, 100, 101, 
102, 103, 104, 105, 106, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 
122, 1, 2, 6, 7, 10, 11, 14, 15, 17, 18, 21, 22, 29, 30, 
36, 37, 41, 42, 45, 46, 49, 50, 56, 57, 58, 59, 62, 63, 64, 
67, 68, 69, 70, 71, 74, 75, 78, 79, 83, 84, 85, 92, 93, 94, 
95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 111, 112, 
113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 
1, 2, 6, 7, 10, 11, 14, 15, 17, 18, 21, 22, 29, 30, 36, 
37, 41, 42, 45, 46, 49, 50, 51, 57, 58, 59, 62, 63, 64, 67, 
71, 74, 75, 78, 79, 81, 82, 85, 86, 97, 98, 99, 100, 101, 102, 
103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 118, 
119, 120, 121, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 17, 18, 
21, 22, 29, 30, 31, 36, 37, 41, 42, 45, 46, 49, 50, 51, 57, 
58, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 78, 79, 80, 
82, 83, 84, 85, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 
108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 93, 
94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 
124, 125, 126, 93, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 
110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 126, 100, 101, 102, 103, 
104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 
102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 
104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 109, 81, 1, 2, 
3, 4, 5, 6, 51, 52, 62, 63, 69, 70, 71, 72, 73, 74, 80, 
81, 102, 103, 1, 2, 5, 6, 20, 21, 51, 52, 62, 63, 69, 70, 
103, 1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 19, 20, 23, 24, 
25, 26, 27, 33, 34, 35, 36, 39, 40, 41, 42, 44, 45, 46, 47, 
48, 51, 52, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 69, 70, 
76, 77, 78, 80, 81, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 
99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 1, 2, 3, 4, 5, 
9, 10, 13, 14, 16, 17, 20, 23, 24, 26, 27, 32, 33, 36, 37, 
39, 40, 44, 48, 54, 55, 58, 59, 62, 63, 69, 70, 71, 72, 73, 
76, 77, 80, 81, 84, 88, 91, 92, 95, 96, 98, 99, 102, 103, 106, 
107, 109, 110, 1, 2, 5, 6, 9, 10, 13, 14, 16, 17, 20, 23, 
24, 25, 26, 33, 34, 35, 36, 37, 39, 40, 44, 45, 46, 47, 48, 
49, 54, 55, 58, 59, 62, 63, 69, 70, 76, 80, 81, 84, 85, 86, 
87, 88, 89, 91, 92, 95, 96, 98, 99, 102, 103, 106, 107, 108, 109, 
1, 2, 6, 7, 9, 10, 13, 14, 17, 18, 19, 20, 25, 26, 27, 
32, 33, 36, 37, 39, 40, 44, 54, 55, 58, 59, 62, 63, 69, 70, 
76, 80, 81, 84, 91, 92, 95, 96, 98, 99, 102, 103, 108, 109, 110, 
1, 2, 5, 6, 9, 10, 12, 13, 14, 16, 23, 26, 27, 32, 33, 
36, 37, 39, 40, 44, 45, 48, 49, 54, 55, 58, 59, 62, 63, 69, 
70, 76, 80, 81, 84, 85, 88, 89, 91, 92, 95, 96, 98, 99, 102, 
103, 106, 109, 110, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 
14, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 32, 33, 34, 35, 
36, 37, 39, 40, 45, 46, 47, 48, 54, 55, 58, 59, 62, 63, 64, 
69, 70, 76, 80, 81, 85, 86, 87, 88, 91, 92, 95, 96, 99, 100, 
101, 103, 106, 107, 108, 109, 110, 16, 20, 21, 16, 17, 18, 19, 20, 
21, 1, 2, 3, 4, 5, 6, 43, 44, 45, 46, 47, 48, 112, 113, 
1, 2, 3, 4, 5, 6, 43, 44, 45, 46, 47, 48, 112, 113, 1, 
2, 6, 7, 9, 10, 13, 14, 17, 19, 20, 21, 28, 29, 30, 34, 
35, 36, 37, 43, 44, 51, 52, 53, 57, 58, 59, 65, 66, 67, 68, 
72, 73, 74, 80, 81, 84, 85, 91, 92, 93, 94, 98, 99, 100, 101, 
104, 105, 107, 108, 112, 113, 1, 2, 5, 6, 9, 10, 13, 14, 17, 
18, 19, 20, 21, 27, 28, 30, 31, 34, 37, 38, 43, 44, 45, 46, 
47, 50, 51, 53, 54, 57, 58, 59, 64, 65, 68, 71, 72, 74, 75, 
80, 81, 84, 85, 90, 91, 92, 94, 95, 97, 98, 101, 102, 104, 105, 
106, 107, 108, 109, 112, 113, 1, 2, 3, 4, 5, 9, 10, 13, 14, 
17, 21, 30, 31, 34, 35, 43, 44, 45, 46, 47, 53, 54, 57, 68, 
69, 71, 72, 73, 80, 81, 84, 85, 90, 91, 94, 95, 101, 102, 104, 
105, 108, 109, 112, 113, 1, 2, 5, 6, 9, 10, 13, 14, 17, 21, 
27, 28, 29, 30, 31, 34, 35, 36, 37, 38, 43, 44, 50, 51, 52, 
53, 54, 57, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 80, 81, 
84, 85, 90, 91, 98, 99, 100, 101, 102, 104, 105, 108, 109, 112, 1, 
2, 6, 9, 10, 13, 14, 17, 21, 26, 27, 30, 31, 37, 38, 43, 
44, 49, 50, 53, 54, 57, 64, 65, 68, 69, 74, 75, 80, 81, 84, 
85, 90, 91, 94, 95, 97, 98, 101, 102, 104, 105, 108, 109, 1, 2, 
6, 7, 9, 10, 11, 12, 13, 14, 17, 21, 26, 27, 28, 29, 30, 
31, 34, 35, 37, 38, 43, 44, 49, 50, 51, 52, 53, 54, 57, 64, 
65, 67, 68, 69, 71, 72, 74, 75, 80, 81, 82, 83, 84, 85, 91, 
92, 93, 94, 95, 97, 98, 100, 101, 102, 104, 105, 108, 109, 112, 113, 
1, 2, 6, 7, 10, 11, 13, 14, 17, 21, 27, 28, 29, 30, 31, 
35, 36, 37, 43, 44, 50, 51, 52, 53, 54, 57, 65, 66, 68, 69, 
72, 73, 74, 81, 82, 84, 85, 92, 93, 94, 98, 99, 101, 102, 104, 
105, 108, 109, 112
])

welcome_screen_y_bmp = array.array('I', [
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 
5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 
6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 
8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 
9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 
11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 
11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 
12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 
13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 
13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 
14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 
14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 
15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 
15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 
16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 
17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 
17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 
18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 
18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 
19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 
19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 
19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 
21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 
21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 
21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 
21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 
21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 
22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 
23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 
25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 
25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 
25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 
25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 
26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 
26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 
26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 
26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 
27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 
27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 
27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 
28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 
29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 
30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 
31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 35, 36, 36, 
36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 
36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 
37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 
38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 
38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 
38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 
38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 
39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 
39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 
39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 
39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 
40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 
41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 
41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 
41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 
42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 
42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 
43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 
43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 
43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 
43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 45, 45, 45, 45, 45, 
45, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 
53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 
54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 
54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 
54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 
54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 
55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 
55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 
55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 
55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 56, 
56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 
56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 
56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 
57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 
57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 
57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 
58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 
58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 
58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 
59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 
59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 
59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 
59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 
60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 
60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 
60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 
60, 60, 60, 60
    ])

