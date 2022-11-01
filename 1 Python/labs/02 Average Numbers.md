# Lab 2: Average Numbers

### Git Setup:
```sh
> git checkout main
> git pull
> git checkout -b your-name/python/lab01
```

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember `len` will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.
```python
nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

```

## Version 2

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

```python
nums = []
nums.append(5)
print(nums)
```

Below is an example input/output:


```
> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4
```

### Git Add, Commit & Push:
```sh
> git add files-to-be-added
> git commit -m "your commit message goes here"
> git push -u origin your-name/python/lab01
```
Then go to the repository to create a PR.
