# Python code to read data from selected.csv matching with the labels in grouped_labels.csv

import pandas as pd

# Read selected.csv
selected_df = pd.read_csv('selected.csv')

# Read grouped_labels.csv
grouped_labels = {
    'Ethnicity': {'white', 'brown', 'black'},
    'Gender': {'male', 'female'},
    'Service': {'nail polish', 'mens colour', 'eyelash lift', 'makeup services', 'hair highlights', 'cosmetic dentistry', 'grooming', 'chemical peels', 'facial waxing', 'barber', 'bohemian twist', 'body massage', 'lifestyle photography', 'teeth', 'acupunture', 'hair styling', 'wispy', 'beauty training', 'acne treatment', 'beauty treatment', 'hard', 'updos', 'awakening programs', 'nail services', 'cat eye', 'crystal healing', 'pilates classes', 'skin care services', 'physical therapy', 'soft wax', 'pedicure', 'manicure', 'vitamin injections', 'weaves', 'wrinkles', 'mens wax', 'box braids', 'knotless braids', 'bridal services', 'reflexology', 'perm', 'plasma fibrolast', 'cornrows', 'dermal fillers', 'hair treatments', 'fitness programs', 'eyelash services', 'tatto service', 'gel nails', 'microblading', 'sugaring', 'cooking classes', 'strip wax', 'restorative dentistry', 'yoga and meditation', 'anesthesia', 'bridal', 'waxing services', 'stretch mark treatment', 'cosmetic injectables', 'facial treatments', 'wig services', 'eyebrow services', 'spa', 'medical services', 'tanning services', 'artistic services', 'body waxing', 'light therepy', 'hair saloons', 'eyebrow waxing', 'bikini wax', 'vajacial', 'permanent makeup', 'energy healing', 'extension services', 'dreads', 'braids', 'eyebrows', 'eyelash fills', 'beauty services', 'personal training', 'piercing services', 'kids services', 'portrait photography', 'barber services', 'meditation', 'crochet', 'wedding services', 'group services', 'body contouring', 'group fitness classes', 'cupping therapy', 'passion twist', 'lower body wax', 'lip treatments', 'feed ins', 'sew ins', 'loc services', 'business photography', 'kinky twist', 'hard wax', 'discount services', 'mens braids', 'detoxification services', 'iv therepy', 'alternative therapy', 'bohemian box braids', 'grocery shopping', 'dreadlocs', 'microneedling', 'weight loss services', 'upper body wax', 'microdermabrasion', 'locs'},
    'Age': {'kids', 'middle', 'old'},
    'Photo_Ratio': {'potrait', 'landscape', 'square'},
    'Subject_Placement': {'right', 'center', 'left'}
}

# Function to match labels with categories
def match_labels(categories):
    matched_labels = {'Ethnicity': set(), 'Gender': set(), 'Service': set(), 'Age': set(), 'Photo_Ratio': set(), 'Subject_Placement': set()}
    for category, labels in grouped_labels.items():
        for label in labels:
            if any(label.lower() == category.lower() for category in categories):
                matched_labels[category].add(label.lower())
    return matched_labels

# Apply the function to each row in selected_df
selected_df['matched_labels'] = selected_df['selected_categories'].apply(eval).apply(match_labels)

# Print the results
# print(selected_df[['image_name', 'selected_categories', 'matched_labels']].head())

# Save the results to a new csv file
selected_df.to_csv('database_feed.csv', index=False)



