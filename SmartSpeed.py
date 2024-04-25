import speedtest

def speed_test():
    # Create Speedtest object
    st = speedtest.Speedtest()
    
    # Perform speed test
    print("Running speed test. This may take a moment...")
    st.get_best_server()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    
    # Print results
    print("Download Speed: {:.2f} Mbps".format(download_speed))
    print("Upload Speed: {:.2f} Mbps".format(upload_speed))

if __name__ == "__main__":
    speed_test()
