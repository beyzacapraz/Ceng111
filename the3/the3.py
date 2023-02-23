from math import exp
def forward_pass(network, X):
    def linear(X, weights):
        X2 = []
        for i in weights:
            result = 0
            n = 0
            while n < len(X):
                result += X[n]*i[n]
                n += 1
            X2.append(result)
        return X2
    def relu(X):
        for i in X:
            if max(0, i) == 0:
                X[X.index(i)] = 0
        return X
    def sigmoid(X):
        for i in X:
            if -700 >= i:
                X[X.index(i)] = 0
            elif i < 700:
                X[X.index(i)] = 1 / (1 + 1 / exp(i))
            else:
                X[X.index(i)] = 1
        return X
    for i in network:
        if type(i) != list:
            if i[0] == "r":
                relu(X)
            elif i[0] == "s":
                sigmoid(X)
        else:
            linear(X, i[1])
            X = linear(X, i[1])
    return X






















