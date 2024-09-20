import numpy as np
import csv
import matplotlib.pyplot as plt
import imutils

heatmap = np.load('output/heatmapdata.npy', allow_pickle=True)


# data_dict = strokes.item()

# # Open a CSV file for writing
# with open('strokeprediction.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write the header
#     writer.writerow(['Video_Frame', 'Forehand_Probability', 'Backhand_Probability', 'Serve_Probability', 'Stroke'])
    
#     # Write the data
#     for key, value in data_dict.items():
#         if isinstance(value, dict) and 'probs' in value aned isinstance(value['probs'], np.ndarray):
#             row = [key] + value['probs'].tolist() + [value['stroke']]
#             writer.writerow(row)
print((heatmap))





def display_heatmap(heatmap, image=None, cmap=plt.cm.bwr, title=''):
        """
        Display the heatmap on top of an image
        """

        if image is not None:
            h, w = image.shape

            heatmap = imutils.resize(heatmap, w, h)
            heatmap = heatmap[:h, :w]
            image = imutils.resize(image, 500)

        heatmap = imutils.resize(heatmap, 500)

        fig = plt.figure(figsize=(5,10))
        # Define the canvas as 1*1 division, and draw on the first position
        ax = fig.add_subplot()

        # Draw and select the color fill style of the heat map, select hot here

        if image is not None:
            im2 = ax.imshow(image, cmap='gray')
            pass
        im = ax.imshow(heatmap, alpha=0.5, cmap=cmap)
        plt.title(title)
        # Add the color scale bar on the right
        # plt.colorbar(im)
        # Add title

        plt.setp(ax, xticks=[], yticks=[])
        # show
        plt.show()

display_heatmap(heatmap)