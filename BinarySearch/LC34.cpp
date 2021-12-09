/*
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
*/

class Solution {
public:
    
    int firstOcc(vector<int>& nums, int target){
        int s=0,e=nums.size()-1,mid,ans;
        
        while(s<=e){
            
            mid=(s+e)/2;
            
            if(nums[mid] == target){
                ans=mid;
                e=mid-1;
            }
            else if(nums[mid] > target)
                e=mid-1;
            else
                s=mid+1;
        }
        return ans;
    }
    
    int lastOcc(vector<int>& nums, int target){
        int s=0,e=nums.size()-1,mid,ans;
        
        while(s<=e){
            
            mid=(s+e)/2;
            
            if(nums[mid] == target){
                ans=mid;
                s=mid+1;
            }
            else if(nums[mid] > target)
                e=mid-1;
            else
                s=mid+1;
        }
        return ans;   
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int f,l;
        f=firstOcc(nums, target);
        l=lastOcc(nums,target);
        vector <int> ans{f,l};
        return ans;  
    }
};

/*
//equal range gives both lower_bound and upper_bound as pair
        auto [lower, upper] = equal_range(begin(nums),end(nums),target);
        
        //if both lower_bound and upper_bound are equal element is not present
        if(lower == upper) return vector<int>{-1,-1};
        
        //if element is present returning its position
        return vector<int>{(int)(lower-nums.begin()),(int)(upper-nums.begin()-1)};
        
        */
