import numpy as np

def MNK_direct (x, y, pl = None, lab = None, color = None):

    '''
    Parameters
    ---------- 
    x:     np.array(1, n_objects) - array of x-axis values
    y:     np.array(1, n_objects) - array of y-axis values
    pl:    matplotlib.pyplot
    lab:   string - label on your plot
    color: string - color of your plot

    Returns
    -------
    k:  float - slope of function
    qk: float - error of k
    '''

    x = np.array(x)
    y = np.array(y)

    k  = np.mean(x * y) / np.mean(x * x)
    qk = np.sqrt(1 / (len(x) - 1) * ((np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - (np.mean(x)) ** 2) - k ** 2))

    if pl:
        pl.scatter(x, y, label = lab, marker='o', c = color)
        pl.plot ([x[0], x[len(x)-1]], [fx(x[0], k, 0), fx(x[len(x)-1], k, 0)], c = color)


    return [k, qk]

def fx(x, k, b):

    '''
    Parameters
    ----------
    x: np.array(1, n_objects) or float - points 
    k:  float - slope of function
    b:  float - bias term of function
    
    Returns
    -------
    f(x): float - value of function in this point
    '''

    return x * k + b

def MNK (x, y, err_x = None, err_y = None, pl = None, lab = None, color = None):
    '''
    Parameters
    ---------- 
    x:     np.array(1, n_objects) - array of x-axis values
    y:     np.array(1, n_objects) - array of y-axis values
    err_x: np.array(1, n_objects) - array of errors on x-axis
    err_y: np.array(1, n_objects) - array of errors on y-axis
    pl:    matplotlib.pyplot
    lab:   string - label on your plot
    color: string - color of your plot

    Returns
    -------
    k:  float - slope of function
    qk: float - error of k
    b:  float - bias term of function
    qb: float - error of b
    '''

    x = np.array(x)
    y = np.array(y)

    p = np.polyfit(x, y, 1)

    k = p[0]
    b = p[1]

    qk = np.sqrt( np.abs(1 / (len(x) - 2) * ((np.mean(y ** 2) - np.mean(y) ** 2) / (np.mean(x ** 2) - (np.mean(x)) ** 2) - k ** 2)))

    qb = qk * np.sqrt(np.mean(x ** 2))

    if pl:
        pl.errorbar(x, y, err_y, err_x, label = lab, marker='o', linestyle = '', c = color)
        pl.plot ([min(x), max(x)], [fx(min(x), k, b), fx(max(x), k, b)], c = color)

    return [k, abs(qk), b, abs(qb)]