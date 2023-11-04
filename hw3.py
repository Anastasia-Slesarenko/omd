class CountVectorizer():
    """
    Convert a collection of text documents to a matrix of token counts.

    The number of features will be equal to the vocabulary size found
    by analyzing the data.
    """

    def __init__(self) -> None:
        self._vocabulary = {}

    def fit_transform(self, corpus: list[str]) -> list:
        """"
        Learn the vocabulary dictionary and return document-term matrix.

        Args:
            corpus (List[str]): An list which consists of strings.

        Returns:
            count_matrix (list): Document-term matrix.
        """
        if not (
            isinstance(corpus, list) and
            all(isinstance(sent, str) for sent in corpus)
        ):
            raise ValueError(
                'A list containing strings is expected.'
            )

        if self._vocabulary:
            self._vocabulary = {}

        corpus = [sentence.lower().split() for sentence in corpus]
        for sentence in corpus:
            for word in sentence:
                self._vocabulary[word] = 0

        count_matrix = []
        for sentence in corpus:
            dict_ = self._vocabulary.copy()
            for word in sentence:
                dict_[word] += 1
            count_matrix.append(list(dict_.values()))
        return count_matrix

    def get_feature_names(self) -> list[str]:
        """
        Get output feature names for transformation.

        Returns:
            list[str]: Transformed feature names.
        """
        if not self._vocabulary:
            raise 'The dictionary is empty. Run the fit_transform first.'
        return list(self._vocabulary.keys())


if __name__ == '__main__':
    vectorizer = CountVectorizer()
