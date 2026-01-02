import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import solvers

#this was originally done in noteable. So it was set out slightly differently. However, I have tried
#to keep all the important sections. In addition, I am following the brief we were given for the project
#And using the template we were provided. Which includes some hints and occasional extra comments that are not my own.

#1. Load and Prepare Data

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Set the path to the dataset you are using.
# Examples: 'boardgame_data.csv', 'spotify.csv', 'coffee.csv'
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
DATASET_PATH = 'spotify_data.csv'  # change as needed

# Load
df = pd.read_csv(DATASET_PATH)
print("Loaded:", DATASET_PATH)
display(df.head())
print(df.info())

# Select numeric columns
numeric_df = df.select_dtypes(include=[np.number]).copy()
n_sample_points, n_attributes = numeric_df.shape

print("Numeric shape:", numeric_df.shape)
display(numeric_df.head())

#2. Visualise Data

numeric_df.hist()
plt.tight_layout()


#3. Write a function to normalise the dataset

def normalise_dataset(X):
    """
    Standardise the dataset attribute-wise to zero mean and unit variance.

    Parameters
    ----------
    X : np.ndarray
        2D array of shape (n_sample_points, n_attributes).

    Returns
    -------
    X_norm : np.ndarray
        Normalised data with zero mean and unit variance per attribute.
        Shape: (n_sample_points, n_attributes).
    mu : np.ndarray
        Attribute means. Shape: (n_attributes,).
    sigma : np.ndarray
        Attribute standard deviations. Shape: (n_attributes,).

    Notes
    -----
    * Compute mu as the mean of each column
    * Compute sigma as the standard deviation along each column
    * For attributes where sigma == 0 (constant attributes), set the normalized
      values to zero.
    * Do not use external ML libraries (sklearn, etc.).
    """
    # TODO: implement
 
    #mean = sum(values) / total n
    #sd = square root ( sum ((x i - mean))2 / total n)
    #normalise = x i - mean / sd

    #defining stuff
    n_sample_points, n_attributes = X.shape
    mu = np.zeros([n_attributes])
    sigma = np.zeros([n_attributes])
    X_norm = np.empty_like(X)

    for i in range(0, n_attributes):
        mu_total = 0 
        for j in range(0, n_sample_points):
            #adds up every value in the column
            mu_total = mu_total + X[j, i]
        mean = mu_total / n_sample_points
        #work out the variance, by iterating through every value in the column, (Value - mean) squared. Add all them up. then divide by n-1
        var = (sum((X[k, i] - mean)**2  for k in range(n_sample_points))) / (n_sample_points-1)
        #this uses the sample variance, because the data we have doesn't represent every song used in the world, its just a sample of them. 
        #raise to power of 1/2 so square root 
        sd = var ** 0.5
        #save mean in the mean array, and sd in the sigma array
        mu[i] = mean
        sigma[i] = sd
        for j in range(0, n_sample_points):
            if (sd == 0):
                #if var = 0, set value to 0
                X_norm[j, i] = 0
            else:
                #normalise using Xi - mu / sigma
                X_norm[j, i] = (X[j, i] - mean) / sd

    return X_norm, mu, sigma


#testings
#X = np.array([[1, 0], [3, 4], [5, 8]])
#X_norm, m, s = normalise_dataset(X)
#Y, mu, sigma = normalise_dataset = normalise_dataset(X_norm)
#print(X_norm)
#print(mu)
#print(sigma)

#X_norm, mu1, sigma1 = normalise_dataset(pd.DataFrame.to_numpy(numeric_df))
#Y_norm, mu2, sigma2 = normalise_dataset(X_norm)

#print(X_norm)
#print(mu2)
#print(sigma2)

#4. Covariance Analysis

def covariance(X: np.ndarray) -> np.ndarray:
    """
    Compute the sample covariance matrix. You should not assume that the data is normalised in this function.

    Parameters
    ----------
    X : np.ndarray
        2D array of shape (n_sample_points, n_attributes).

    Returns
    -------
    np.ndarray
        Covariance matrix of shape (n_attributes, n_attributes).
        Element (i, j) represents the covariance between attributes i and j.

    Notes
    -----
    * The resulting matrix should be symmetric: C[i,j] == C[j,i].
    * Do not use numpy.cov() or other pre-built covariance functions.
    """

    X_norm, mu, sigma = normalise_dataset(X)
    #print(mu)
    n, m = X.shape
    #print(n)
    #print(m)
    C = np.zeros([m,m])

    #1/n-1 x sum of (Xki- mui) (Xkj-muj)


    for i in range(0, m):
        for j in range(0, m):
            #implements fomula. and changes C. k from 0 to n. 
            C[i, j] = sum((X[k, i] - mu[i])*(X[k, j] - mu[j]) for k in range(0, n)) / (n-1)

    return C
#X = np.array([[1, 0], [3, 4], [5, 8]])
#covariance(X)

# Prepare a numpy array for covariance / PCA
X = numeric_df.values.astype(float)

# Compute covariance
X_std, _, _ = normalise_dataset(X)
C = covariance(X_std)

# Visualise covariance as a heatmap
# TODO implement
# HINT https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

fig, ax = plt.subplots()
im = ax.imshow(C)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)

ax.set_title("Spotify Data")
fig.tight_layout()
plt.show()

#this is where I am up to. 

#next sections are:
#5. EigenValues and eigenvector computations

def sorted_eigenvalues(A):
    """
    Compute eigenvalues and eigenvectors of A using the Gram–Schmidt QR
    algorithm, then sort them by decreasing eigenvalue.

    Parameters
    ----------
    A : np.ndarray
        A symmetric square matrix of shape (n, n).
        Typically this will be a covariance matrix.

    Returns
    -------
    eigenvalues : np.ndarray
        1D array of length n containing eigenvalues sorted in descending order.
    eigenvectors : np.ndarray
        2D array of shape (n, n) where column i (eigenvectors[:, i]) is the
        normalized eigenvector corresponding to eigenvalues[i].
        Eigenvectors are sorted to match the order of eigenvalues.

    Notes
    -----
    * Use solvers.gram_schmidt_eigen(A) to compute the eigendecomposition.
      This function returns (eigenvalues, eigenvectors, iterations).
      You only need the first two return values.
    * The function MODIFIES the input matrix A in place, so always pass A.copy().
    * The returned eigenvalues and eigenvectors are UNSORTED.
    * Sort the eigenvalues in descending order (largest first).
    * Reorder the eigenvector columns to match the sorted eigenvalue order.
    * Do not use numpy.linalg.eig, numpy.linalg.eigh, or similar functions.

    Example
    -------
    If A has eigenvalues [2.5, 5.1, 1.3], this function should return:
        eigenvalues = [5.1, 2.5, 1.3]
        eigenvectors[:, 0] corresponds to eigenvalue 5.1
        eigenvectors[:, 1] corresponds to eigenvalue 2.5
        eigenvectors[:, 2] corresponds to eigenvalue 1.3
    """
    
    ...
# TODO Compute eigenvalues and eigenvectors of covariance and print first 5 eigenvalues
...

#6. check orthonormality
# TODO implement test of orthonormality
...
#7. explained variance
# TODO plot of cummulative explained variance
...
#8. projection
# TODO plot of PC1 vs PC2 coloured by interesting attribute
...
