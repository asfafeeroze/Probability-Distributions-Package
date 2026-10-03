import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials

    """


    def __init__(self, prob=0.5, size=20):

        #  TODO: store the probability of the distribution in an instance variable p
        #  TODO: store the size of the distribution in an instance variable n
        self.p = prob
        self.n = size

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        Distribution.__init__(self, mu=self.mean, sigma=self.stdev)

        pass

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        
        mean = self.p * self.n 

        self.mean = mean

        return mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        
        stdev = math.sqrt(self.n * self.p * (1 - self.p))

        self.stdev = stdev

        return stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        self.n = len(self.data) # Total number of trials
        self.p = sum(self.data) / self.n # prob of +ve outcome

        # recalculate mean and standard deviation
        self.calculate_mean()
        self.calculate_stdev()

        return self.p, self.n 

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        zeros = self.data.count(0)
        ones = self.data.count(1)

        x = [0,1]
        y = [zeros, ones]

        plt.bar(x, y)

        plt.title("Binomial Distribution")
        plt.xlabel("Outcome")
        plt.ylabel("Count")

        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        combinations = math.comb(self.n, k) 
        success_probability = self.p**k
        failure_probability = (1 - self.p) ** (self.n - k)

        return combinations * success_probability * failure_probability


    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot 
            list: y values for the pdf plot

        """

        successes = list(range(0, self.n + 1))
        x = range(0, self.n+1)
        y = [] # Stores the pdf

        for k in x:
            y.append(self.pdf(k))

        # plot the PMF 
        plt.bar(x,y)

        plt.title("Binomial Distribution PMF")
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")

        plt.show()

        return x,y


    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, "p values are not equal"
        except AssertionError as error:
            raise

        new_n = self.n + other.n
        result = Binomial(prob = self.p, size = new_n)
        
        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"

        pass