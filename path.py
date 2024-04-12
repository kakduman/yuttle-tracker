
import math

path = [41.315763,-72.924481,41.31606,-72.924399,41.316233,-72.924349,41.317398,-72.92403,41.318773,-72.923655,41.31923,-72.92353,41.319612,-72.923425,41.319904,-72.923365,41.320041,-72.923349,41.320205,-72.923334,41.320283,-72.92333,41.320695,-72.923337,41.321182,-72.923353,41.322066,-72.923381,41.322202,-72.923385,41.32263,-72.923371,41.322951,-72.923361,41.323255,-72.923352,41.323728,-72.92334,41.323946,-72.923309,41.324611,-72.923192,41.324828,-72.923149,41.325362,-72.922935,41.325649,-72.922811,41.325867,-72.922716,41.326294,-72.922532,41.326904,-72.922279,41.326977,-72.922251,41.327192,-72.922191,41.32779,-72.922063,41.328264,-72.922001,41.328413,-72.921993,41.328564,-72.921975,41.329277,-72.921808,41.330303,-72.921563,41.330607,-72.921487,41.330658,-72.92135,41.330264,-72.919054,41.329991,-72.917478,41.329963,-72.917326,41.329936,-72.917167,41.329426,-72.914252,41.329492,-72.914221,41.329492,-72.914221,41.329426,-72.914252,41.328832,-72.914533,41.328261,-72.914802,41.327462,-72.915181,41.326144,-72.915808,41.324738,-72.916478,41.3247,-72.916633,41.3247,-72.916633,41.324602,-72.916541,41.324218,-72.916711,41.323771,-72.91691,41.32305,-72.917264,41.322535,-72.917509,41.322078,-72.917724,41.321454,-72.918016,41.321258,-72.918109,41.320798,-72.918326,41.320449,-72.91849,41.319606,-72.918888,41.31937,-72.919004,41.31924,-72.919067,41.31813,-72.919601,41.317882,-72.919721,41.317718,-72.919799,41.317106,-72.920086,41.31645,-72.920394,41.315954,-72.920627,41.315833,-72.920684,41.315652,-72.920771,41.315425,-72.920878,41.314879,-72.921137,41.314697,-72.921221,41.314306,-72.9214,41.314011,-72.921577,41.313513,-72.921939,41.313213,-72.922189,41.312589,-72.922661,41.312422,-72.922783,41.312128,-72.922997,41.311419,-72.92351,41.311061,-72.923768,41.311023,-72.923887,41.311241,-72.924411,41.311471,-72.924956,41.311729,-72.92558,41.311544,-72.925548,41.310808,-72.926078,41.31078,-72.926099,41.310689,-72.926165,41.310162,-72.92656,41.309481,-72.927059,41.308385,-72.927856,41.307363,-72.928621,41.307213,-72.92873,41.306324,-72.929409,41.306068,-72.929604,41.305971,-72.929677,41.305269,-72.930198,41.305073,-72.930346,41.304635,-72.930676,41.304255,-72.930938,41.304124,-72.931041,41.303684,-72.931366,41.303605,-72.931447,41.303523,-72.931534,41.303251,-72.931717,41.302782,-72.932056,41.302174,-72.932515,41.301985,-72.933146,41.301918,-72.933392,41.301879,-72.933531,41.302169,-72.933689,41.302731,-72.933997,41.303167,-72.934234,41.303548,-72.934443,41.303843,-72.934604,41.30398,-72.934897,41.30429,-72.934674,41.304896,-72.934266,41.304972,-72.934216,41.305515,-72.933818,41.305623,-72.933731,41.30622,-72.933289,41.306352,-72.933192,41.30648,-72.933101,41.306643,-72.932985,41.306972,-72.932752,41.307233,-72.932562,41.307984,-72.932012,41.308471,-72.931642,41.308653,-72.931516,41.309083,-72.93122,41.309593,-72.930851,41.310651,-72.930065,41.310687,-72.929939,41.310175,-72.928727,41.309481,-72.927059,41.310162,-72.92656,41.310657,-72.926189,41.310736,-72.926131,41.310806,-72.926079,41.311544,-72.925548,41.311729,-72.92558,41.311898,-72.925587,41.312748,-72.925353,41.313761,-72.92507,41.313933,-72.925017,41.314323,-72.924893,41.315077,-72.924668,41.315442,-72.924569,41.315763,-72.924481]

points = [(41.315763, -72.924481), (41.31606, -72.924399), (41.316233, -72.924349), (41.317398, -72.92403), (41.318773, -72.923655), (41.31923, -72.92353), (41.319612, -72.923425), (41.319904, -72.923365), (41.320041, -72.923349), (41.320205, -72.923334), (41.320283, -72.92333), (41.320695, -72.923337), (41.321182, -72.923353), (41.322066, -72.923381), (41.322202, -72.923385), (41.32263, -72.923371), (41.322951, -72.923361), (41.323255, -72.923352), (41.323728, -72.92334), (41.323946, -72.923309), (41.324611, -72.923192), (41.324828, -72.923149), (41.325362, -72.922935), (41.325649, -72.922811), (41.325867, -72.922716), (41.326294, -72.922532), (41.326904, -72.922279), (41.326977, -72.922251), (41.327192, -72.922191), (41.32779, -72.922063), (41.328264, -72.922001), (41.328413, -72.921993), (41.328564, -72.921975), (41.329277, -72.921808), (41.330303, -72.921563), (41.330607, -72.921487), (41.330658, -72.92135), (41.330264, -72.919054), (41.329991, -72.917478), (41.329963, -72.917326), (41.329936, -72.917167), (41.329426, -72.914252), (41.329492, -72.914221), (41.329492, -72.914221), (41.329426, -72.914252), (41.328832, -72.914533), (41.328261, -72.914802), (41.327462, -72.915181), (41.326144, -72.915808), (41.324738, -72.916478), (41.3247, -72.916633), (41.3247, -72.916633), (41.324602, -72.916541), (41.324218, -72.916711), (41.323771, -72.91691), (41.32305, -72.917264), (41.322535, -72.917509), (41.322078, -72.917724), (41.321454, -72.918016), (41.321258, -72.918109), (41.320798, -72.918326), (41.320449, -72.91849), (41.319606, -72.918888), (41.31937, -72.919004), (41.31924, -72.919067), (41.31813, -72.919601), (41.317882, -72.919721), (41.317718, -72.919799), (41.317106, -72.920086), (41.31645, -72.920394), (41.315954, -72.920627), (41.315833, -72.920684), (41.315652, -72.920771), (41.315425, -72.920878), (41.314879, -72.921137), (41.314697, -72.921221), (41.314306, -72.9214), (41.314011, -72.921577), (41.313513, -72.921939), (41.313213, -72.922189), (41.312589, -72.922661), (41.312422, -72.922783), (41.312128, -72.922997), (41.311419, -72.92351), (41.311061, -72.923768), (41.311023, -72.923887), (41.311241, -72.924411), (41.311471, -72.924956), (41.311729, -72.92558), (41.311544, -72.925548), (41.310808, -72.926078), (41.31078, -72.926099), (41.310689, -72.926165), (41.310162, -72.92656), (41.309481, -72.927059), (41.308385, -72.927856), (41.307363, -72.928621), (41.307213, -72.92873), (41.306324, -72.929409), (41.306068, -72.929604), (41.305971, -72.929677), (41.305269, -72.930198), (41.305073, -72.930346), (41.304635, -72.930676), (41.304255, -72.930938), (41.304124, -72.931041), (41.303684, -72.931366), (41.303605, -72.931447), (41.303523, -72.931534), (41.303251, -72.931717), (41.302782, -72.932056), (41.302174, -72.932515), (41.301985, -72.933146), (41.301918, -72.933392), (41.301879, -72.933531), (41.302169, -72.933689), (41.302731, -72.933997), (41.303167, -72.934234), (41.303548, -72.934443), (41.303843, -72.934604), (41.30398, -72.934897), (41.30429, -72.934674), (41.304896, -72.934266), (41.304972, -72.934216), (41.305515, -72.933818), (41.305623, -72.933731), (41.30622, -72.933289), (41.306352, -72.933192), (41.30648, -72.933101), (41.306643, -72.932985), (41.306972, -72.932752), (41.307233, -72.932562), (41.307984, -72.932012), (41.308471, -72.931642), (41.308653, -72.931516), (41.309083, -72.93122), (41.309593, -72.930851), (41.310651, -72.930065), (41.310687, -72.929939), (41.310175, -72.928727), (41.309481, -72.927059), (41.310162, -72.92656), (41.310657, -72.926189), (41.310736, -72.926131), (41.310806, -72.926079), (41.311544, -72.925548), (41.311729, -72.92558), (41.311898, -72.925587), (41.312748, -72.925353), (41.313761, -72.92507), (41.313933, -72.925017), (41.314323, -72.924893), (41.315077, -72.924668), (41.315442, -72.924569), (41.315763, -72.924481)]

distances = [0.03372748688682788, 0.01968473576777483, 0.132253222021187, 0.156067513218485, 0.05187723918960578, 0.043372119527012414, 0.0328532746709875, 0.015292192132227388, 0.0182789413435867, 0.008679634634256805, 0.04581603925879415, 0.05416841113644014, 0.09832412218120178, 0.015126198724707128, 0.04760578642131299, 0.03570333870071538, 0.03381161161870137, 0.05260474559533266, 0.024378328088502026, 0.07458728983472888, 0.02439500637681476, 0.06200882258708316, 0.033550734578080804, 0.025505524334443332, 0.049904348532502744, 0.07104277443224809, 0.008447245400150167, 0.02442624913322577, 0.06734808740865428, 0.05296004128984678, 0.016581505152629086, 0.016857570833335476, 0.08049894714346335, 0.1159056054885356, 0.03439374603795638, 0.012767691103027114, 0.1966530294312664, 0.13504904073452212, 0.013068057454199611, 0.013611474069636299, 0.24991785482869627, 0.007781973793137276, 0.0, 0.007781973793137276, 0.07009352836422157, 0.06734830195434391, 0.09431285928904505, 0.15562613903546058, 0.16604930529126366, 0.01361553512569393, 0.0, 0.013332940125457724, 0.044996849364238006, 0.05240847868080033, 0.08544795067776408, 0.060810440372346695, 0.053894615294368606, 0.07354573090283763, 0.02313663689817021, 0.05426492300211808, 0.04115285660849686, 0.09945557680560473, 0.02797298348553293, 0.015383032902262598, 0.1312358870617732, 0.029340892253171783, 0.01936450046415242, 0.07214897686891214, 0.07734640159953929, 0.05848487070709121, 0.014271917423069271, 0.02139769034395702, 0.02677644742512048, 0.06445074887300625, 0.021418978795976543, 0.04597568385100974, 0.03597965104016736, 0.06309111660591303, 0.039354271841925095, 0.07980241135592586, 0.021181473442485835, 0.037258337411404156, 0.0897281309997135, 0.04526598174871309, 0.010800073520704374, 0.05003044993225483, 0.05221213100858612, 0.059491756857163285, 0.020743960324484313, 0.09304437756629338, 0.0035735237240888305, 0.011522878401205257, 0.06724866664221428, 0.08643603626343667, 0.13886587432484576, 0.13037357123015034, 0.019002335078366316, 0.11396679968553025, 0.032796499871158534, 0.01239018910549406, 0.08937044841655992, 0.025056293038018505, 0.05596295737710975, 0.0475853542416188, 0.016917688506166245, 0.055952971123147975, 0.01108809140790434, 0.011659815404861, 0.03388858623441166, 0.059342697740147596, 0.07772221979187806, 0.056745142995130816, 0.021858233922048245, 0.012394666089687385, 0.034843024232901754, 0.06758063294137197, 0.05236735582834758, 0.045821474593747955, 0.035452370616382116, 0.028828488242952463, 0.03918156099338886, 0.07551230045380547, 0.009426537034609541, 0.06892628042306873, 0.01403665727331917, 0.07595940130960392, 0.016765523684183284, 0.016135475296342537, 0.02055212210701788, 0.041437859566677955, 0.03307770090855217, 0.09530978276919905, 0.06235007645852338, 0.022810420774332353, 0.053827628625403155, 0.0645435510123267, 0.1347221169121786, 0.011259521480022374, 0.1161413603641147, 0.1592629615772484, 0.08643603626343667, 0.06316463785741178, 0.010031613718568724, 0.008913386668995852, 0.09327972867895086, 0.020743960324484313, 0.01880103518528646, 0.09651517781438428, 0.11509360759374807, 0.019631091970949466, 0.04458548027557571, 0.08592107299413786, 0.04141978542208232, 0.03644236325879506]

total_distances = sum(distances)

def haversine(lat1, lon1, lat2, lon2):
    # Radius of Earth in kilometers
    R = 6371

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

def find_progress(lat, lon, points=points, distances=distances, total_distance=total_distances):
    '''
    Takes in a latitude and a longitude.
    Returns the progress along the path and the closest point on the path.
    '''
    min_distance = float('inf')
    closest_point = None

    accumulated_distance = 0
    closest_segment_fraction = 0

    # Find the closest point on the path
    for i in range(1, len(points)):
        segment_distance = distances[i-1]
        start_point = points[i-1]
        end_point = points[i]

        # Calculate the projection (closest point on the current segment)
        # Simplified calculation assuming flat Earth for short distances
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        # if the segment is not a point
        if dx != 0 or dy != 0:
            # Calculate the projection of the point onto the segment
            t = ((lat - start_point[0]) * dx + (lon - start_point[1]) * dy) / (dx * dx + dy * dy)
            # Clamp to segment endpoints
            t = max(0, min(1, t))
            closest_lat = start_point[0] + t * dx
            closest_lon = start_point[1] + t * dy
            distance_to_point = haversine(lat, lon, closest_lat, closest_lon)
            if distance_to_point < min_distance:
                min_distance = distance_to_point
                closest_point = (closest_lat, closest_lon)
                closest_segment_fraction = accumulated_distance + t * segment_distance

        accumulated_distance += segment_distance

    # Calculate progress as a decimal
    progress = closest_segment_fraction / total_distance
    return progress, closest_point


def prepare_data(path):
    points = [(path[i], path[i+1]) for i in range(0, len(path), 2)]
    distances = []
    total_distance = 0 
    # Calculate total distance and distances between each point
    for i in range(1, len(points)):
        dist = haversine(points[i-1][0], points[i-1][1], points[i][0], points[i][1])
        total_distance += dist
        distances.append(dist)
        
    print(points)
    print(distances)
    print(sum(distances))
    
# # Example usage
# lat, lon = 41.326914, -72.922289
# progress, closest_point = find_progress(lat, lon)
# print(f"Progress: {progress}, Closest point on path: {closest_point}")
