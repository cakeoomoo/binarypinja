/*
 * =====================================================================================
 *
 *       Filename:  test.c
 *
 *    Description:  for reverse engineering 
 *
 *        Version:  1.0
 *        Created:  11/13/2018 06:50:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


int main()
{

    int array_1[] = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10};

    for(int i = 0;i < 40;i++)

        printf("%d\n",array_1[i]);  // ans is 40.0

    return 0;
}


