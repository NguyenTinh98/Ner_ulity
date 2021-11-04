### Get sentences error:
### tabel (word, pos, ner, ner_predict, error)
def make_error(num_sent, y_pred, x_test):
    """
    function make_error help get data predict Nertag error of a sentence
    :y_pred is output predict of Model from x_test, y_predict shape (len(X_test), 1), is list [predict_ners]
    :x_test is input into model, shape (m, 1), m: amount words in a sentence, each word is tuple (word, true_pos, true_ner)
    :output: return data frame (word, true_pos, true_ner, predict_ner, is_error)
    """
    
    sentence_info = []
    for index in range(len(x_test)):
        word = x_test[index]
        true_ner = word[1]

        if true_ner == y_pred[index]:
            is_error = 0
            sentence_info.append((num_sent, word[0], word[2], word[1], y_pred[index], is_error))
        else:
            is_error = 1
            sentence_info.append((num_sent, word[0], word[2], word[1], y_pred[index], is_error))
    return   sentence_info 

def make_errors(Y_pred, X_test):
    df = pd.DataFrame([], columns = ["#sent","word", "true_pos", "true_ner", "predict_ner", "is_error"])
    sentences_info = []
    for index in range(len(X_test)):
        x_test = X_test[index]
        y_pred = Y_pred[index]
        sentence_info = make_error(index, y_pred, x_test)
        df = df.append(pd.DataFrame(sentence_info,  columns = ["#sent", "word", "true_pos", "true_ner", "predict_ner", "is_error"]))
    return df
    

def  analyst_error(num_sent, y_pred, x_test):
    """
    function make_error help get data predict Nertag error of a sentence
    :y_pred is output predict of Model from x_test, y_predict shape (len(X_test), 1), is list [predict_ners]
    :x_test is input into model, shape (m, 1), m: amount words in a sentence, each word is tuple (word, true_pos, true_ner)
    :output: return data frame (word, true_pos, true_ner, predict_ner, is_error)
    """
    
    sentence_info = []
    for index in range(len(x_test)):
     
#         print(x_test[index][2] , y_pred[index])
        if x_test[index][1] != y_pred[index]:
             
            
            if index == 0:
                sentence_info.append((num_sent, 
                  [x_test[index][0], x_test[index + 1][0], x_test[index + 2][0]],
                  [x_test[index][2], x_test[index + 1][2], x_test[index + 2][2]], 
                  [x_test[index][1], x_test[index + 1][1], x_test[index + 2][1]], 
                  [y_pred[index],y_pred[index + 1],y_pred[index + 2]],
                     x_test[index][1]))
            
            if index >= 1 and index !=len(x_test) -1  :
                sentence_info.append((num_sent, 
                  [x_test[index - 1][0], x_test[index][0], x_test[index + 1][0]],
                  [x_test[index - 1][2], x_test[index][2], x_test[index + 1][2]], 
                  [x_test[index - 1][1], x_test[index][1], x_test[index + 1][1]], 
                  [y_pred[index - 1],y_pred[index],y_pred[index + 1]],
                                      x_test[index][1]))
          
            if index ==len(x_test) - 1  :
                    sentence_info.append((num_sent, 
                      [x_test[index - 2][0], x_test[index][0], x_test[index][0]],
                      [x_test[index - 2][2], x_test[index][2], x_test[index][2]], 
                      [x_test[index - 2][1], x_test[index][1], x_test[index ][1]], 
                      [y_pred[index - 2],y_pred[index-1],y_pred[index]],
                                          x_test[index][1]))
    return   sentence_info 
    
def analyts_errors(Y_pred, X_test):
    """
    Phân tích lỗi theo cụm từ gần nhất
    :Y_pred: outputs của X_test
    : X_test: m câu dự đoán
    :output: return dataframe chứa thông tin các từ xung quanh từ bị "dự đoán sai", hiện tại: 2 từ xung quanh
    """
    df = pd.DataFrame([], columns = ["#sent","words", "true_poss", "true_ners", "predict_ners", "error_labels"])
    sentences_info = []
    for index in range(len(X_test)):
        x_test = X_test[index]
        y_pred = Y_pred[index]
        sentence_info = analyst_error(index, y_pred, x_test)
        df = df.append(pd.DataFrame(sentence_info,  columns = ["#sent","words", "true_poss", "true_ners", "predict_ners","error_labels"]))
    return df    