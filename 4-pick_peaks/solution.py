"""
https://www.codewars.com/kata/pick-peaks/python
"""

def pick_peaks(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] >= arr[i+1]:
            if arr[i] == arr[i+1]:  # <-- this could be a plateau, but we need to check
                for val in arr[i+1:]:
                    if val < arr[i]:
                        pos.append(i)
                        peaks.append(arr[i])
                        break
                    if val > arr[i]:
                        break
            else:
                pos.append(i)
                peaks.append(arr[i])
    return {'pos': pos, 'peaks': peaks}
