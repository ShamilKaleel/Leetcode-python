class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        for i,n in enumerate(numbers):
            next_value=target-n
            if next_value in numbers:
                if len(output)>0 and numbers.index(next_value)!=i:
                    output.append(i+1)
                if len(output)==0:
                    output.append(i+1)
                
                # indices = [j for j, num in enumerate(numbers) if num == target-n]
                # if len(indices)>1:
                #     output.append(indices[1])
                # else:
                #    output.append(numbers.index(target-n))     
        return output    
                