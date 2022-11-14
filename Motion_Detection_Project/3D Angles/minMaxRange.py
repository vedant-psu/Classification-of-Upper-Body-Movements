# find the hill which has greatest height
# greatest height=top point height - lowest point height
# lowest point can be left slant/right slant side
# And it has a minimum height point on that slant side

'''
Example 
  /\
 /  \
/    \
      \

For the above hill it has max. height 4 because right slant is at much lower depth
than left slant side. However, if the minimum is on left slant side then 
we have to consider the left slant portion for our problem.
'''

import csv

## file_name is the file that contains angles for each frame
with open('fine_name.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for col in range(6): 
        #store [frame, angle] pairs
        list = []
        # find the min and max values
        minAngle=400
        maxAngle=-400
        for row in csv_reader:
            if line_count > 0:
                list.append([row[1], row[col+2]])
                minAngle=min(minAngle, row[col+2])
                maxAngle=max(maxAngle, row[col+2])

        # minAngle=1
        # maxAngle=11
        # list=[[1,1],[2,1.5],[3,2],[4,4],[5,6],[6,3],[7,5],[8,7],[9,8],[10,9],[11,10],[12,11]]
        # Answer: Required region starts at coordinate: (6,3) and ends at (12,11) while the minimum Angle is at ((1, 1))
        ## Two cases
        # 1. left slant
        size=len(list)
        min_left=400
        min_left_frame=-1
        max_left=-400
        max_left_frame=-1
        start_left=-1
        start_left_frame=-1
        diff=0
        minCurRange=400
        for i in range(size):
            frame=list[i][0]
            angle=list[i][1]
            height=angle-minCurRange
            if(min_left>angle):
                min_left=angle
                min_left_frame=frame
            if((i==0 or list[i-1][1]<angle) and (i+1==len(list) or list[i+1][1]<angle)):
                if(diff<height):
                    max_left_frame=frame
                    max_left=angle 
                minCurRange=400
                continue

            if(minCurRange>angle):
                minCurRange=angle
                start_left=angle
                start_left_frame=frame

        # 2. right slant
        min_right=400
        min_right_frame=-1
        max_right=-400
        max_right_frame=-1
        start_right=-1
        start_right_frame=-1
        diff=0
        minCurRange=400

        list.reverse()
        for i in range(size):
            frame=list[i][0]
            angle=list[i][1]
            height=angle-minCurRange
            if(min_right>angle):
                min_right=angle
                min_right_frame=frame
            if((i==0 or list[i-1][1]<angle) and (i+1==len(list) or list[i+1][1]<angle)):
                if(diff<height):
                    max_right_frame=frame
                    max_right=angle 
                minCurRange=400
                continue
                
            if(minCurRange>angle):
                minCurRange=angle
                start_right_frame=frame
                start_right=angle

        if(min_left!=400 and min_left_frame!=-1 and max_left!=-400 and max_left_frame!=-1 and start_left!=-1 and start_left_frame!=-1):
            print(f'\tRequired region starts at coordinate: ({start_left_frame},{start_left}) and ends at ({max_left_frame},{max_left}) while the minimum Angle is at ({min_left_frame, min_left})')
        else: 
            print(f'\tRequired region starts at coordinate: ({start_right_frame},{start_right}) and ends at ({max_right_frame},{max_right}) while the minimum Angle is at ({min_right_frame, min_right})')





                