def inheritance(Descriptions):
    main_lst = []
    inheritance_lst = []
    for i in Descriptions:
        main_lst.append(i.split())
    n = None
    d = None
    for j in main_lst:
        if j[0] == "DECEASED":
            n = float(j[2])
            d = j[1]
    def check_departed(name):
        result = False
        for i in main_lst:
            if i[0] == "DEPARTED" and i[1] == name:
                result = True
        return result

    def check_empty(lst):
        if type(lst) == list:
            k = str(lst)
            if k.strip("[]"):
                return check_empty(lst[0]) + check_empty(lst[1:])
            else:
                return False
        return True

    def find_spouse(d):
        lst2 = []
        for i in main_lst:
            if i[0] == "MARRIED" and (i[1] == d or i[2] == d):
                lst2 += i
        if not lst2:
            inheritance_lst.append([])
        else:
            for j in lst2[1:3]:
                if j != d:
                    if not check_departed(j):
                        inheritance_lst.append(j)
                    else:
                        inheritance_lst.append([])

    def find_children(d):
        children = []
        for i in main_lst:
            if i[0] == "CHILD" and (i[1] == d or i[2] == d):
                children += i[3:]
        return children
    def find_children_recursive(children):
        if len(children) == 0:
            return []
        elif not check_departed(children[0]):
            return [children[0]] + find_children_recursive(children[1:])
        else:
            return [find_children_recursive(find_children(children[0]))] + find_children_recursive(children[1:])

    def pg1(n, lst):
        for i in lst:
            if not check_empty(i): lst.remove(i)
        if len(lst) == 0:
            return []
        elif type(lst[0]) != list:
            c = n / len(lst)
            return [(lst[0], c)] + pg1(n-c, lst[1:])
        else:
            for i in lst[0]:
                if not check_empty(i): lst[0].remove(i)
            c = n / len(lst)
            return pg1(c, lst[0]) + pg1(n-c, lst[1:])

    def find_parent(d):
        parent = []
        for i in main_lst:
            if i[0] == "CHILD":
                for j in i[3:]:
                    if j == d:
                        parent.append(i[1])
                        parent.append(i[2])
        return parent

    def find_parent_recursive(parent):
        if not parent:
            return []
        elif not check_departed(parent[0]):
            return [parent[0]] + find_parent_recursive(parent[1:])
        else:
            parent_child = find_children(parent[0])
            if d in parent_child:
                parent_child.remove(d)
            return [find_children_recursive(parent_child)] + find_parent_recursive(parent[1:])

    def find_grandparent(parent):
        grand_parent = []
        for i in parent:
            lst = []
            for j in main_lst:
                if j[0] == "CHILD":
                    for k in j[3:]:
                        if i == k:
                            lst.append(j[1])
                            lst.append(j[2])
            grand_parent.append(lst)
        return grand_parent

    def find_grandparent_recursive(grand_parent):
        if not grand_parent:
            return []
        elif type(grand_parent[0]) == list:
            return find_grandparent_recursive(grand_parent[0]) + find_grandparent_recursive(grand_parent[1:])
        elif not check_departed(grand_parent[0]):
            return [grand_parent[0]] + find_grandparent_recursive(grand_parent[1:])
        else:
            grand_parent_child = find_children(grand_parent[0])
            for i in find_parent(d):
                if i in grand_parent_child:
                    grand_parent_child.remove(i)
            return [find_grandparent_recursive(grand_parent_child)] + find_grandparent_recursive(grand_parent[1:])

    find_spouse(d)
    final_lst= []
    y = find_children(d)
    z = find_children_recursive(y)
    for i in z:
        if not check_empty(i): z.remove(i)
    inheritance_lst.append(z)
    if inheritance_lst[1] != []:
        if inheritance_lst[0] != []:
            final_lst.append((inheritance_lst[0],n/4))
            n = 3*n/4
            final_lst += pg1(n,inheritance_lst[1])
        else:
            final_lst += pg1(n, inheritance_lst[1])
    elif inheritance_lst[1] == []:
        t = find_parent(d)
        k = find_parent_recursive(t)
        for j in k:
            if not check_empty(j): k.remove(j)
        inheritance_lst.append(k)
        if check_empty(inheritance_lst[2]):
            if inheritance_lst[0] != []:
                final_lst.append((inheritance_lst[0], n / 2))
                n = n/2
                final_lst += pg1(n,inheritance_lst[2])
            else:
                final_lst += pg1(n, inheritance_lst[2])
        elif not check_empty(inheritance_lst[2]):
            m = find_grandparent(t)
            p = find_grandparent_recursive(m)
            for i in p:
                if not check_empty(i): p.remove(i)
            inheritance_lst.append(p)
            if check_empty(inheritance_lst[3]):
                if inheritance_lst[0] != []:
                    final_lst.append((inheritance_lst[0], 3*n / 4))
                    n = n/4
                    final_lst += pg1(n, inheritance_lst[3])
                else:
                    final_lst += pg1(n, inheritance_lst[3])
            elif not check_empty(inheritance_lst[3]):
                if inheritance_lst[0] != []:
                    final_lst.append((inheritance_lst[0],n))
    str_lst = []
    num = 0
    for i in final_lst:
        for j in i:
            if type(j) == str: str_lst.append(j)
    name = None
    for i in str_lst:
        if str_lst.count(i) > 1:
            name = i
            break
    for j in final_lst:
        if j[0] == name:
            num += j[1]
    new_tuple = (name, num)
    if list(set(str_lst)) != str_lst:
        for k in final_lst:
            if k[0] == name:
                final_lst.insert(final_lst.index(k), new_tuple)
                final_lst.remove(k)

        final_lst = list(set(final_lst))
    return final_lst

















