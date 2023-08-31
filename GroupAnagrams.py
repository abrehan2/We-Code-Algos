def groupAnagrams(strs):

    if len(strs) == 0:
        print("Please add elements in the array")

    result = {}

    for i in strs:

        str = "".join(sorted(i))

        if str not in result:
            result[str] = []

        result[str].append(i)

    return result.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
