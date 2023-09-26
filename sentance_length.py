def main():
    # write your code here

    sentence = (input("Write a sentence --> "))
    num_chars = len(sentence)
    chars_round_ten= (num_chars //10)


    print("The number of characters in your sententence is about",( chars_round_ten * 10), "characters.")

    

    
    return

if __name__ == '__main__':
    main()