number = int(input("Enter a integer number: "))
is_less_tan_ten = number < 10
is_odd = number % 2 != 0
group_a = is_less_tan_ten and not is_odd
group_b = not is_less_tan_ten and is_odd
group_both = is_less_tan_ten and is_odd
empty_group = not is_less_tan_ten and not is_odd

if group_both:
    print("The number is a member of group A and B")
elif group_a:
    print("The number is a member of group A")
elif group_b:
    print("The number is a member of group B")
else:
    print("The number is not a member of any group")
