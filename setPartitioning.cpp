#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <time.h>
#include <string>
using namespace std;

int main()
{
    srand(time(NULL));
    time_t start, currentTime, end;
    start = time(NULL);
    int numSets = 3;
    int numCaps = 35;
    int sumOfCaps = 0;
    cout << "numSets = " << numSets << " : numCaps = " << numCaps << ": ";
    int listOfCaps[numCaps];
    
    for(int j = 0; j < numCaps; j++){
        
        listOfCaps[j] = rand() % 100 + 1;
        sumOfCaps = sumOfCaps + listOfCaps[j];
    }
    
    int histogram[(100 * numCaps)];
    for(int i = 0; i < (100 * numCaps); i++){
        histogram[i] = 0;
    }
    
    int targetPerSet = sumOfCaps / numSets;
    for(int x = 0; x < numCaps; x++)
        cout << listOfCaps[x] << ' ';
 
    cout << endl << "Target per Set: " << targetPerSet << endl;

    int minAbsDiff = 5000000;
    int maxAbsDiff = 0;
    int absoluteDiff, count, hours, mins, secs, runtime, set0, set1, set2;//, set3, set4, set5, set6, set7, set8, set9;
    string best, worst, num;
    long long int randomPermutations= pow(2, 35);
    srand(time(0));
    for(long long int k = 0; k < randomPermutations; k++){
        
        num = "";
        for(int y = 0; y < numCaps; y++){
            
            int randIndex = rand() % 3;
            if(randIndex == 0)
                num = num + "0";
            else if(randIndex == 1)
                num = num + "1";
            else if(randIndex == 2)
                num = num + "2";
            else if(randIndex == 3)
                num = num + "3";
            else if(randIndex == 4)
                num = num + "4";
            else if(randIndex == 5)
                num = num + "5";
            else if(randIndex == 6)
                num = num + "6";
            else if(randIndex == 7)
                num = num + "7";
            else if(randIndex == 8)
                num = num + "8";
            else
                num = num + "9";
        }
        
        set0 = 0;
        set1 = 0;
        set2 = 0;        
        set3 = 0;
        set4 = 0;
        set5 = 0;
        set6 = 0;
        set7 = 0;
        set8 = 0;
        set9 = 0;
        
        count = 0;
        for(int l = 0; l < num.length(); l++){
            if (num[l] == '0')
                set0 = set0 + listOfCaps[count];            
            else if (num[l] == '1')   
                set1 = set1 + listOfCaps[count];
            else if (num[l] == '2')   
                set2 = set2 + listOfCaps[count];
            else if (num[l] == '3')   
                set3 = set3 + listOfCaps[count];
            else if (num[l] == '4')   
                set4 = set4 + listOfCaps[count];
            else if (num[l] == '5')               
                set5 = set5 + listOfCaps[count];
            else if (num[l] == '6')   
                set6 = set6 + listOfCaps[count];
            else if (num[l] == '7')   
                set7 = set7 + listOfCaps[count];
            else if (num[l] == '8')   
                set8 = set8 + listOfCaps[count];            
            else 
                set9 = set9 + listOfCaps[count];
            
            count++;
            
        }

        absoluteDiff = abs(targetPerSet - set0) + abs(targetPerSet - set1) + abs(targetPerSet - set2) + abs(targetPerSet - set3) + abs(targetPerSet - set4) 
                     + abs(targetPerSet - set5) + abs(targetPerSet - set6) + abs(targetPerSet - set7) + abs(targetPerSet - set8) + abs(targetPerSet - set9);
        histogram[absoluteDiff]++;
        if(absoluteDiff < minAbsDiff){
            minAbsDiff = absoluteDiff;
            best = num;
        }
        if(absoluteDiff > maxAbsDiff){
            maxAbsDiff = absoluteDiff;
            worst = num;
        }
        if(k % 50000000 == 0){ 
            cout << "Current combination: " << k << '\n' << endl;
            currentTime = time(NULL);
            runtime =  difftime(currentTime, start);
            hours = runtime / 3600;
            mins = (runtime - (hours * 3600)) / 60;
            secs = (runtime - (hours * 3600) - (mins * 60)) % 60;
            cout << "current runtime: " << hours << " h: " << mins << " m: " << secs << " s" << endl;
            
        }
    }
    cout << "min: " << minAbsDiff << endl;
    cout << "max: " << maxAbsDiff << endl;
    currentTime = time(NULL);
    runtime =  difftime(currentTime, start);
    hours = runtime / 3600;
    mins = (runtime - (hours * 3600)) / 60;
    secs = (runtime - (hours * 3600) - (mins * 60)) % 60;
    cout << "Final runtime: " << hours << " h: " << mins << " m: " << secs << " s" << endl;
    
    ofstream myFile;
    myFile.open("base3(35)random(1).xlsx");
    myFile << "Capabilities: ";
    for(int m = 0; m < 35; m++){
        myFile << listOfCaps[m] << " ";
    }
    myFile << "\n";
    myFile << "One of the best produced: " << best << " with an absolute difference of " << minAbsDiff << "\n";
    myFile << "One of the worst produced: " << worst << " with an absolute difference of " <<  maxAbsDiff << "\n";
    myFile << "Final runtime: " << hours << " h: " << mins << " m: " << secs << " s\n";
    for(int x = minAbsDiff; x <= maxAbsDiff; x += 2){
        myFile << histogram[x] << "\n";
    }
    myFile.close();
    return 0;
}


