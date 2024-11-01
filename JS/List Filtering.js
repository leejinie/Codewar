function filter_list(l) {
    var numbersOnly = l.filter(item => typeof item === 'number');
    return(numbersOnly)
  }