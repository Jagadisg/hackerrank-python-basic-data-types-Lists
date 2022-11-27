if __name__ == '__main__':
    N = int(input())
    list1 = []
    ans = []
    for i in range(N):
        list1.append(input().split())
    for i in list1:
        if i[0] == "insert":
            a = int(i[1])
            b = int(i[2])
            ans.insert(a,b)
        elif i[0] == "remove":
            e = int(i[1])
            # print(e)
            ans.remove(e)
        elif i[0] == "append":
            j = int(i[1])
            # print(j)
            ans.append(j)
        elif i[0] == "print":
            print(ans)
        elif i[0] == "sort":
            ans.sort()
        elif i[0] == "pop":
            ans.pop()
        elif i[0] == "reverse":
            ans.reverse()
    # print(list1)
            