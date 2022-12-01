# Import your tree classes and timeit
from bst import BinarySearchTree, BinaryTree
import timeit
import random  # For producing random numbers

def generate_randint_list(length=100, seed=42, max=1000):
    """Generates a list of randomly generated integers

    Args:
        length (integer): length of the list
        seed (integer): seed value

    Returns:
        list: returns the list of random integers
    """

    rand_list = []
    random.seed(seed)

    for i in range(length):
        rand_list.append(random.randint(1,max))
    
    # print("Random Integer list: ", rand_list)
    
    return rand_list


def generate_tree(data, TreeObject):
    """Generates the tree out of input list data and TreeObject

    Args:
        data (list): list of data to be used as input.
        TreeObject (object): TreeObject as defined by user's class

    Returns:
        tree: Returns the tree instance
    """
    
    tree = TreeObject(data[0])

    for i in range(1, len(data)):
        tree.insert(data[i])
    
    return tree


# This block is almost similar in use to C language's main() function
if __name__ == '__main__':


    

    # Test cases
    test_case_1 = {'search value': 282,
                  'data length': 10,
                  'max': 1000
                  }
    
    test_case_2 = {'search value': 883,
                  'data length': 100,
                  'max': 1000
                  }
    
    test_case_3 = {'search value': 546,
                  'data length': 300,
                  'max': 1000
                  }

    test_case_4 = {'search value': 66,
                  'data length': 1000,
                  'max': 1000
                  }
    
    test_case_5 = {'search value': 2014,
                  'data length': 10000,
                  'max': 10000
                  }

    test_case_6 = {'search value': 62554,
                  'data length': 100000,
                  'max': 100000
                  }


    # ======= UPDATE ACTIVE TEST CASES HERE =======
    active_testcase = test_case_6
    # =============================================
    
        
    data = generate_randint_list(active_testcase['data length'], max = active_testcase['max'])
    bst_tree = generate_tree(data, BinarySearchTree)
    bin_tree = generate_tree(data, BinaryTree)
    test_n = 100
    
    # Lines or blocks of code to be tested
    # BST
    bst_test_stmt = f"print(bst_tree.search({active_testcase['search value']}))"  
    bst_result = timeit.timeit(stmt=bst_test_stmt, globals=globals(), number=test_n)
    print(f'Execution time for Binary Search Tree is {bst_result/test_n} seconds.')
    
    # Binary Trees
    bin_test_stmt = f"print(bin_tree.search({active_testcase['search value']}))"  
    bin_result = timeit.timeit(stmt=bin_test_stmt, globals=globals(), number=test_n)
    print(f'Execution time for Binary Tree is {bin_result/test_n} seconds.')