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


if __name__ == '__main__':
    # should support finding peaks
    print pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}

    # should support finding peaks, but should ignore peaks on the edge of the array
    print pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}

    # should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau
    print pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}

    # should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau
    print pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos":[2,4], "peaks":[3,2]}

    # should support finding peaks, but should ignore peaks on the edge of the array
    print pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}
