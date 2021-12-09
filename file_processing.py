
def get_sentences(text):
    '''(str) -> list
    Given a string returns a list of strings each representing one of the sentences.
    
    >>> text = "I am hungry. Starving even."
    >>> get_sentences(text)
    ['I am hungry', 'Starving even']
    
    >>> text = "What time is it. It is laundry day."
    >>> get_sentences(text)
    ['What time is it', 'It is laundry day']
    '''
    #splits the text and joins again with three spaces, each time for a different punctuation ending.
   
    split3 = text.split('\n')
    join3 = '   '.join(split3)
    #if the line ends with a punctuation, omits that punctuation from the final text
    if join3[-1] == '!' or join3[-1] == '.' or join3[-1] == '?' or join3[-1] == ' ' or join3[-1] == '\n':
        join3 = join3[:-1]
    #creates the final text by creating a list from the previous string    
    final_text = join3.split('   ')
    return final_text


def get_word_breakdown(text):
    '''(str) -> (list)
    Given a string returns a 2D lists of strings, with each sublist containing strings representing words from each sentence.
    >>> text = 'i went to the park. it was fun.'
    >>> get_word_breakdown(text)
    [['i', 'went', 'to' , 'the', 'park'], ['it', 'was', 'fun']
    
    >>> text = 'nice shirt. i like it'
    >>> get_word_breakdown(text)
    [['nice', 'shirt'], ['i' ,'like', 'it'] 
    '''
    #creates a list of punctuation
    punctuation = [',', '-', '--', ':', ';', '"', "'"]
    #removes extra lines
    text = text.split('\n')
    while '' in text:
        text.remove('')
    text = ' '.join(text)
    #removes extra tabs
    text = text.split('\t')
    while '' in text:
        text.remove('')
    text = ' '.join(text)
    #removes extra spaces
    text = text.split(' ')
    while '' in text:
        text.remove('')
    text = ' '.join(text)
    #makes text all lowercase
    text = text.lower()
    #replaces all punctuation with empty string
    for p in punctuation:
        text = text.replace(p, '')
    #formats into sentences using get_sentences function
    sentences = get_sentences(text)
    list1 = list()
    final_list = list()
    #creates sub-lists in list1
    for i in sentences:
        new_list = [i]
        list1.append(new_list)
    
    #seperates words in each sublist in list1
    for i in list1:
        join1 = ''.join(i)
        split1 = join1.split(' ')
        final_list.append(split1)
        
    return final_list


