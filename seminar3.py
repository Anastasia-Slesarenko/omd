from math import log


class CountVectorizer():
    """
    Convert a collection of text documents to a matrix of token counts.

    The number of features will be equal to the vocabulary size found
    by analyzing the data.
    """

    def __init__(self) -> None:
        self._vocabulary = {}

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """"
        Learn the vocabulary dictionary and return document-term matrix.

        Args:
            corpus (List[str]): An list which consists of strings

        Returns:
            count_matrix (list[list[int]]): Document-term matrix
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

        corpus = [document.lower().split() for document in corpus]
        for document in corpus:
            for word in document:
                self._vocabulary[word] = 0

        count_matrix = []
        for document in corpus:
            dict_ = self._vocabulary.copy()
            for word in document:
                dict_[word] += 1
            count_matrix.append(list(dict_.values()))
        return count_matrix

    def get_feature_names(self) -> list[str]:
        """
        Get output feature names for transformation.

        Returns:
            list[str]: Transformed feature names
        """
        if not self._vocabulary:
            raise 'The dictionary is empty. Run the fit_transform first.'
        return list(self._vocabulary.keys())


class TfidfTransformer():
    """
    Transform a count matrix to tf-idf representation.
    Ttf-idf means term frequency times inverse document-frequency
    """

    def fit_transform(
            self,
            count_matrix: list[list[int]]
            ) -> list[list[float]]:
        """
        Fit the transformer to the count matrix and return a tf-idf matrix.

        Args:
            count_matrix (list[list[int]]): Document-term matrix

        Returns:
            list[list[float]]: Term Frequency-Inverse Document Frequency matrix
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tfidf_matrix = []
        for tf_vec in tf_matrix:
            tfidf_matrix.append(
                [tf*idf for tf, idf in zip(tf_vec, idf_matrix)]
            )
        return tfidf_matrix

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Transform the count matrix to a term frequency (TF) matrix.

        Args:
            count_matrix (list[list[int]]): Document-term matrix

        Returns:
            list[list[float]]: Term frequency matrix
        """
        tf_matrix = []
        for document in count_matrix:
            word_count = sum(document)
            tf_vec = [word / word_count for word in document]
            tf_matrix.append(tf_vec)
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """
        Calculate the inverse document frequency (IDF) for each term.

        Args:
            count_matrix (list[list[int]]): Document-term matrix

        Returns:
            list[float]: Inverse document frequency values for terms
        """
        document_count = len(count_matrix)
        idf_matrix = []
        for row in zip(*count_matrix):
            counter = sum(int(num > 0) for num in row)
            idf_matrix.append(
                log((document_count + 1) / (counter + 1)) + 1
            )
        return idf_matrix


class TfidfVectorizer(CountVectorizer):
    """
    Performs the TF-IDF transformation from a provided matrix of counts.
    Ttf-idf means term-frequency times inverse document-frequency.
    """
    def __init__(self, tf_class=TfidfTransformer) -> None:
        super().__init__()
        self.transformer = tf_class()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Fit the vectorizer to the corpus and transform it
        into a TF-IDF representation.

        Args:
        corpus (list[str]): An list which consists of strings

        Returns:
        list[list[float]]:  Term Frequency-Inverse Document Frequency matrix
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    pass
