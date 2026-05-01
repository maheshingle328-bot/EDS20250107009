"""You are provided with the heights of 11 cricket players (in centimeters). Your task is to identify the tallest player, who will be selected as the captain of the team.



Input Format:

The first line of input will contain 11 integers, each representing the height of a player (in centimeters), each separated by a space.



Output Format

The output should be the height (in centimeters) of the tallest player."""
hight=list(map(int,input().split()))
print(max(hight))