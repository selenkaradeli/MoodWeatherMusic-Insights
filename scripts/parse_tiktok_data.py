# example script just a placeholder for now:

import pandas as pd
import os
from datetime import datetime

def parse_browsing_history(file_path):
    """Parse TikTok browsing history from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Link:') and current_date:
                link = line.split('Link:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'link': link
                })
    return pd.DataFrame(data)

def parse_favorite_sounds(file_path):
    """Parse TikTok favorite sounds from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Sound Link:') and current_date:
                link = line.split('Sound Link:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'link': link
                })
    return pd.DataFrame(data)

def parse_favorite_videos(file_path):
    """Parse TikTok favorite videos from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Link:') and current_date:
                link = line.split('Link:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'link': link
                })
    return pd.DataFrame(data)

def parse_like_list(file_path):
    """Parse TikTok liked videos from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Link:') and current_date:
                link = line.split('Link:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'link': link
                })
    return pd.DataFrame(data)

def parse_share_history(file_path):
    """Parse TikTok share history from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Link:') and current_date:
                link = line.split('Link:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'link': link
                })
    return pd.DataFrame(data)

def parse_login_history(file_path):
    """Parse TikTok login history from txt file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        current_date = None
        for line in file:
            line = line.strip()
            if line.startswith('Date:'):
                current_date = line.split('Date:')[1].strip()
            elif line.startswith('Device Model:') and current_date:
                device = line.split('Device Model:')[1].strip()
                data.append({
                    'timestamp': datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S'),
                    'device': device
                })
    return pd.DataFrame(data)

def get_date_range(data_frames):
    """Get the earliest and latest dates from all TikTok data."""
    all_dates = []
    
    for df in data_frames.values():
        if not df.empty and 'timestamp' in df.columns:
            all_dates.extend([df['timestamp'].min(), df['timestamp'].max()])
    
    if all_dates:
        return min(all_dates), max(all_dates)
    return None, None

def main():
    # Output directory
    output_dir = 'data/processed'
    os.makedirs(output_dir, exist_ok=True)
    
    # Parse each data file
    data_types = {
        'browsing_history.txt': parse_browsing_history,
        'favorite_sounds.txt': parse_favorite_sounds,
        'favorite_videos.txt': parse_favorite_videos,
        'like_list.txt': parse_like_list,
        'share_history.txt': parse_share_history,
        'login_history.txt': parse_login_history
    }
    
    all_data = {}
    for filename, parser in data_types.items():
        input_path = os.path.join('data/tiktok_data', filename)
        if os.path.exists(input_path):
            df = parser(input_path)
            output_path = os.path.join(output_dir, f"{filename.replace('.txt', '.csv')}")
            df.to_csv(output_path, index=False)
            all_data[filename] = df
            print(f"Processed {filename} -> {output_path}")
        else:
            print(f"File not found: {input_path}")
    
    # Get and save date range
    start_date, end_date = get_date_range(all_data)
    if start_date and end_date:
        date_range_df = pd.DataFrame({
            'start_date': [start_date],
            'end_date': [end_date]
        })
        date_range_df.to_csv(os.path.join(output_dir, 'date_range.csv'), index=False)
        print(f"\nData range: {start_date} to {end_date}")

if __name__ == "__main__":
    main() 