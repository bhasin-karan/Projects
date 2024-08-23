import cv2 as cv
import numpy as np

class Agent:
    def __init__(self):
        pass

    def Solve(self,problem):

        given_figs = dict()
        option_figs = dict()

        for fig in problem.figures:
            if fig in "ABCDEFGH":
                img = cv.imread(problem.figures[fig].visualFilename, cv.IMREAD_GRAYSCALE)
                ret, given_figs[fig] = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV)
            else:
                img = cv.imread(problem.figures[fig].visualFilename, cv.IMREAD_GRAYSCALE)
                ret, option_figs[fig] = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV)

        if len(given_figs.keys()) == 3:

            #Testing for Column/Row Equality
            def TwoByTwoEquality(given_figs, option_figs):

                sim_AB = cv.matchTemplate(given_figs["A"], given_figs["B"], cv.TM_CCOEFF_NORMED)
                sim_AC = cv.matchTemplate(given_figs["A"], given_figs["C"], cv.TM_CCOEFF_NORMED)
                # cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED) and its use was referred from:
                # https://towardsdatascience.com/image-matching-with-opencvs-template-matching-5df577a3ce2e

                if sim_AB > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["C"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

                elif sim_AC > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["B"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

            # Testing for Column/Row Reflection
            def TwoByTwoReflect(given_figs, option_figs):

                A_flip_y = cv.flip(given_figs["A"], 1)
                A_flip_x = cv.flip(given_figs["A"], 0)
                B_flip_x = cv.flip(given_figs["B"], 0)
                C_flip_y = cv.flip(given_figs["C"], 1)
                sim_reflect_AB = cv.matchTemplate(A_flip_y, given_figs["B"], cv.TM_CCOEFF_NORMED)
                sim_reflect_AC = cv.matchTemplate(A_flip_x, given_figs["C"], cv.TM_CCOEFF_NORMED)

                if sim_reflect_AB > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(C_flip_y, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

                elif sim_reflect_AC > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(B_flip_x, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

            # Testing for 90 degree Rotation
            def TwoByTwoRotate90(given_figs, option_figs):

                A_rotate_90 = cv.rotate(given_figs["A"], cv.ROTATE_90_CLOCKWISE)
                B_rotate_90 = cv.rotate(given_figs["B"], cv.ROTATE_90_CLOCKWISE)
                C_rotate_90 = cv.rotate(given_figs["C"], cv.ROTATE_90_CLOCKWISE)
                sim_rotate_90_AB = cv.matchTemplate(A_rotate_90, given_figs["B"], cv.TM_CCOEFF_NORMED)
                sim_rotate_90_AC = cv.matchTemplate(A_rotate_90, given_figs["C"], cv.TM_CCOEFF_NORMED)

                if sim_rotate_90_AB > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(C_rotate_90, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

                elif sim_rotate_90_AC > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(B_rotate_90, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

            # Testing for 180 degree Rotation
            def TwoByTwoRotate180(given_figs, option_figs):

                A_rotate_180 = cv.rotate(given_figs["A"], cv.ROTATE_180)
                B_rotate_180 = cv.rotate(given_figs["B"], cv.ROTATE_180)
                C_rotate_180 = cv.rotate(given_figs["C"], cv.ROTATE_180)
                sim_rotate_180_AB = cv.matchTemplate(A_rotate_180, given_figs["B"], cv.TM_CCOEFF_NORMED)
                sim_rotate_180_AC = cv.matchTemplate(A_rotate_180, given_figs["C"], cv.TM_CCOEFF_NORMED)

                if sim_rotate_180_AB > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(C_rotate_180, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

                elif sim_rotate_180_AC > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(B_rotate_180, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

            # Testing for 270 degree Rotation
            def TwoByTwoRotate270(given_figs, option_figs):

                A_rotate_270 = cv.rotate(given_figs["A"], cv.ROTATE_90_COUNTERCLOCKWISE)
                B_rotate_270 = cv.rotate(given_figs["B"], cv.ROTATE_90_COUNTERCLOCKWISE)
                C_rotate_270 = cv.rotate(given_figs["C"], cv.ROTATE_90_COUNTERCLOCKWISE)
                sim_rotate_270_AB = cv.matchTemplate(A_rotate_270, given_figs["B"], cv.TM_CCOEFF_NORMED)
                sim_rotate_270_AC = cv.matchTemplate(A_rotate_270, given_figs["C"], cv.TM_CCOEFF_NORMED)

                if sim_rotate_270_AB > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(C_rotate_270, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

                elif sim_rotate_270_AC > 0.80:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(B_rotate_270, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.70:
                            return int(option_fig)

            A_contours, A_hierarchy = cv.findContours(given_figs["A"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            B_contours, B_hierarchy = cv.findContours(given_figs["B"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            C_contours, C_hierarchy = cv.findContours(given_figs["C"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

            #Testing for Fill/Unfill
            def TwobyTwoFill(given_figs, option_figs):

                A_bpx = np.sum(given_figs["A"] == 255)
                B_bpx = np.sum(given_figs["B"] == 255)
                C_bpx = np.sum(given_figs["C"] == 255)

                def contour_areas(contours, hierarchy):
                    contour_areas = []
                    for contour in contours:
                        for n in range(len(contours)):
                            if np.array_equal(contours[n],contour):
                                if hierarchy[0][n][-1] == -1:
                                    contour_areas.append(cv.contourArea(contour))
                    return contour_areas

                A_contour_areas = contour_areas(A_contours, A_hierarchy)
                B_contour_areas = contour_areas(B_contours, B_hierarchy)
                C_contour_areas = contour_areas(C_contours, C_hierarchy)

                if len(A_contour_areas) == len(B_contour_areas) or len(A_contour_areas) == len(C_contour_areas):
                    for A_shape_area in A_contour_areas:
                        AB_ratio = A_shape_area / B_bpx
                        AC_ratio = A_shape_area / C_bpx

                        if 1.10 >= AB_ratio >= 0.90:
                            for C_shape_area in C_contour_areas:
                                for option_fig, option_fig_img in option_figs.items():
                                    option_bpx = np.sum(option_fig_img == 255)
                                    Coption_ratio = C_shape_area / option_bpx
                                    if abs(Coption_ratio - AB_ratio) <= 0.03:
                                        return int(option_fig)

                        elif 1.10 >= AC_ratio >= 0.90:
                            for B_shape_area in B_contour_areas:
                                for option_fig, option_fig_img in option_figs.items():
                                    option_bpx = np.sum(option_fig_img == 255)
                                    Boption_ratio = B_shape_area / option_bpx
                                    if abs(Boption_ratio - AC_ratio) <= 0.03:
                                        return int(option_fig)

                        else:
                            for B_shape_area in B_contour_areas:
                                BA_ratio = B_shape_area / A_bpx

                                if 1.10 >= BA_ratio >= 0.90:
                                    for option_fig, option_fig_img in option_figs.items():
                                        option_contours, option_hierarchy = cv.findContours(option_fig_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                                        option_contours_areas = contour_areas(option_contours, option_hierarchy)
                                        for option_shape_area in option_contours_areas:
                                            optionC_ratio = option_shape_area / C_bpx
                                            if abs(optionC_ratio - BA_ratio) <= 0.03:
                                                return int(option_fig)

                                else:
                                    for C_shape_area in C_contour_areas:
                                        CA_ratio = C_shape_area / A_bpx

                                        if 1.10 >= CA_ratio >= 0.90:
                                            for option_fig, option_fig_img in option_figs.items():
                                                option_contours, option_hierarchy = cv.findContours(option_fig_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                                                option_contours_areas = contour_areas(option_contours, option_hierarchy)
                                                for option_shape_area in option_contours_areas:
                                                    optionB_ratio = option_shape_area / B_bpx
                                                    if abs(optionB_ratio - CA_ratio) <= 0.03:
                                                        return int(option_fig)


            #Testing for Addition/Subtraction of Shapes
            def TwobyTwoContourCounter(given_figs, option_figs):

                def area_counter(contours, hierarchy):
                    contour_areas = []
                    contour_areas_counter = 0
                    for cont in contours:
                        for n in range(len(contours)):
                            if np.array_equal(contours[n], cont):
                                if hierarchy[0][n][-1] == -1:
                                    contour_areas_counter += 1
                                    contour_areas.append(cv.contourArea(cont))
                    return contour_areas, contour_areas_counter

                A_contour_areas = area_counter(A_contours, A_hierarchy)[0]
                B_contour_areas = area_counter(B_contours, B_hierarchy)[0]
                C_contour_areas = area_counter(C_contours, C_hierarchy)[0]
                A_contour_areas_counter = area_counter(A_contours, A_hierarchy)[1]
                B_contour_areas_counter = area_counter(B_contours, B_hierarchy)[1]
                C_contour_areas_counter = area_counter(C_contours, C_hierarchy)[1]

                def area_compare(contour_areas_1, contour_areas_2):
                    similar_areas_count = 0
                    similar_areas_index = []
                    different_areas_count = 0
                    different_areas_index = []
                    different_areas = []
                    for area1 in contour_areas_1:
                        for area2 in contour_areas_2:
                            if abs(area1 - area2) <= 100:
                                similar_areas_count += 1
                                similar_areas_index.append(contour_areas_2.index(area2))
                    for x in range(len(contour_areas_2)):
                        if x not in similar_areas_index:
                            different_areas_count += 1
                            different_areas_index.append(x)
                            different_areas.append(contour_areas_2[x])
                    return different_areas

                def compare_to_options(contour_counter, contour_areas, different_areas):
                    for option_fig, option_img in option_figs.items():

                        option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                        option_contour_areas = area_counter(option_contours, option_hierarchy)[0]
                        option_counter = area_counter(option_contours, option_hierarchy)[1]

                        if contour_counter < option_counter:
                            option_shapes_area = area_compare(contour_areas, option_contour_areas)
                            if option_shapes_area == different_areas:
                                return int(option_fig)
                        elif contour_counter > option_counter:
                            option_shapes_area = area_compare(option_contour_areas, contour_areas)
                            if option_shapes_area == different_areas:
                                return int(option_fig)

                if A_contour_areas_counter < B_contour_areas_counter:
                    different_shapes_areas = area_compare(A_contour_areas, B_contour_areas)
                    possible_answer = compare_to_options(C_contour_areas_counter, C_contour_areas, different_shapes_areas)
                    if type(possible_answer) == int:
                        return possible_answer
                elif A_contour_areas_counter < C_contour_areas_counter:
                    different_shapes_areas = area_compare(A_contour_areas, C_contour_areas)
                    possible_answer = compare_to_options(B_contour_areas_counter, B_contour_areas, different_shapes_areas)
                    if type(possible_answer) == int:
                        return possible_answer
                elif A_contour_areas_counter > B_contour_areas_counter:
                    different_shapes_areas = area_compare(B_contour_areas, A_contour_areas)
                    possible_answer = compare_to_options(C_contour_areas_counter, C_contour_areas, different_shapes_areas)
                    if type(possible_answer) == int:
                        return possible_answer
                elif A_contour_areas_counter > C_contour_areas_counter:
                    different_shapes_areas = area_compare(C_contour_areas, A_contour_areas)
                    possible_answer = compare_to_options(B_contour_areas_counter, B_contour_areas, different_shapes_areas)
                    if type(possible_answer) == int:
                        return possible_answer

            #Fallback function
            def TwobyTwoFallBack(given_figs, option_figs):

                A_bpx = np.sum(given_figs["A"] == 255)
                B_bpx = np.sum(given_figs["B"] == 255)
                C_bpx = np.sum(given_figs["C"] == 255)

                A_tpx = np.sum(given_figs["A"] == 255) + np.sum(given_figs["A"] == 0)
                B_tpx = np.sum(given_figs["B"] == 255) + np.sum(given_figs["B"] == 0)
                C_tpx = np.sum(given_figs["C"] == 255) + np.sum(given_figs["C"] == 0)

                A_dpr = A_bpx / A_tpx
                B_dpr = B_bpx / B_tpx
                C_dpr = C_bpx / C_tpx

                AB_dpr = abs(A_dpr - B_dpr)
                AC_dpr = abs(A_dpr - C_dpr)

                closest_options = dict()

                for option_fig, option_img in option_figs.items():
                    option_bpx = np.sum(option_img == 255)
                    option_tpx = np.sum(option_img == 255) + np.sum(option_img == 0)
                    option_dpr = option_bpx / option_tpx
                    if option_dpr > 0:
                        if A_bpx > B_bpx or A_bpx > C_bpx:
                            closest_options[option_fig] = abs(
                                min((C_dpr - AB_dpr) / option_dpr, (B_dpr - AC_dpr) / option_dpr) - 1)
                        else:
                            closest_options[option_fig] = abs(
                                min((C_dpr + AB_dpr) / option_dpr, (B_dpr + AC_dpr) / option_dpr) - 1)
                for key, val in closest_options.items():
                    if val == min(closest_options.values()):
                        return int(key)

            TwoByTwoEqualityAnswer = TwoByTwoEquality(given_figs, option_figs)
            if type(TwoByTwoEqualityAnswer) == int:
                return TwoByTwoEqualityAnswer

            else:
                TwoByTwoReflectAnswer = TwoByTwoReflect(given_figs, option_figs)
                if type(TwoByTwoReflectAnswer) == int:
                    return TwoByTwoReflectAnswer

                else:
                    TwoByTwoRotate90Answer = TwoByTwoRotate90(given_figs, option_figs)
                    if type(TwoByTwoRotate90Answer) == int:
                        return TwoByTwoRotate90Answer

                    else:
                        TwoByTwoRotate180Answer = TwoByTwoRotate180(given_figs, option_figs)
                        if type(TwoByTwoRotate180Answer) == int:
                            return TwoByTwoRotate180Answer

                        else:
                            TwoByTwoRotate270Answer = TwoByTwoRotate270(given_figs, option_figs)
                            if type(TwoByTwoRotate270Answer) == int:
                                return TwoByTwoRotate270Answer

                            else:
                                TwobyTwoFillAnswer = TwobyTwoFill(given_figs, option_figs)
                                if type(TwobyTwoFillAnswer) == int:
                                    return TwobyTwoFillAnswer
                                else:
                                    TwobyTwoContourCounterAnswer = TwobyTwoContourCounter(given_figs, option_figs)
                                    if type(TwobyTwoContourCounterAnswer) == int:
                                        return TwobyTwoContourCounterAnswer
                                    else:
                                        TwobyTwoFallBackAnswer = TwobyTwoFallBack(given_figs, option_figs)
                                        if type(TwobyTwoFallBackAnswer) == int:
                                            return TwobyTwoFallBackAnswer

        elif len(given_figs.keys()) == 8:

            A_contours, A_hierarchy = cv.findContours(given_figs["A"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            B_contours, B_hierarchy = cv.findContours(given_figs["B"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            C_contours, C_hierarchy = cv.findContours(given_figs["C"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            D_contours, D_hierarchy = cv.findContours(given_figs["D"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            E_contours, E_hierarchy = cv.findContours(given_figs["E"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            F_contours, F_hierarchy = cv.findContours(given_figs["F"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            G_contours, G_hierarchy = cv.findContours(given_figs["G"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
            H_contours, H_hierarchy = cv.findContours(given_figs["H"], cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

            def contour_areas(contours, hierarchy):
                contour_areas = []
                for contour in contours:
                    for n in range(len(contours)):
                        if np.array_equal(contours[n], contour):
                            if hierarchy[0][n][-1] == -1:
                                contour_areas.append(cv.contourArea(contour))
                return contour_areas

            A_contour_areas = contour_areas(A_contours, A_hierarchy)
            B_contour_areas = contour_areas(B_contours, B_hierarchy)
            C_contour_areas = contour_areas(C_contours, C_hierarchy)
            D_contour_areas = contour_areas(D_contours, D_hierarchy)
            E_contour_areas = contour_areas(E_contours, E_hierarchy)
            F_contour_areas = contour_areas(F_contours, F_hierarchy)
            G_contour_areas = contour_areas(G_contours, G_hierarchy)
            H_contour_areas = contour_areas(H_contours, H_hierarchy)

            A_contour_areas_counter = len(A_contour_areas)
            B_contour_areas_counter = len(B_contour_areas)
            C_contour_areas_counter = len(C_contour_areas)
            D_contour_areas_counter = len(D_contour_areas)
            E_contour_areas_counter = len(E_contour_areas)
            F_contour_areas_counter = len(F_contour_areas)
            G_contour_areas_counter = len(G_contour_areas)
            H_contour_areas_counter = len(H_contour_areas)

            A_bpx = np.sum(given_figs["A"] == 255)
            B_bpx = np.sum(given_figs["B"] == 255)
            C_bpx = np.sum(given_figs["C"] == 255)
            D_bpx = np.sum(given_figs["D"] == 255)
            E_bpx = np.sum(given_figs["E"] == 255)
            F_bpx = np.sum(given_figs["F"] == 255)
            G_bpx = np.sum(given_figs["G"] == 255)
            H_bpx = np.sum(given_figs["H"] == 255)

            A_tpx = np.sum(given_figs["A"] == 255) + np.sum(given_figs["A"] == 0)
            B_tpx = np.sum(given_figs["B"] == 255) + np.sum(given_figs["B"] == 0)
            C_tpx = np.sum(given_figs["C"] == 255) + np.sum(given_figs["C"] == 0)
            D_tpx = np.sum(given_figs["D"] == 255) + np.sum(given_figs["D"] == 0)
            E_tpx = np.sum(given_figs["E"] == 255) + np.sum(given_figs["E"] == 0)
            F_tpx = np.sum(given_figs["F"] == 255) + np.sum(given_figs["F"] == 0)
            G_tpx = np.sum(given_figs["G"] == 255) + np.sum(given_figs["G"] == 0)
            H_tpx = np.sum(given_figs["H"] == 255) + np.sum(given_figs["H"] == 0)

            A_dpr = A_bpx / A_tpx
            B_dpr = B_bpx / B_tpx
            C_dpr = C_bpx / C_tpx
            D_dpr = D_bpx / D_tpx
            E_dpr = E_bpx / E_tpx
            F_dpr = F_bpx / F_tpx
            G_dpr = G_bpx / G_tpx
            H_dpr = H_bpx / H_tpx

            # Testing for Column/Row Equality
            def ThreeByThreeEquality(given_figs, option_figs):

                sim_AC = cv.matchTemplate(given_figs["A"], given_figs["C"], cv.TM_CCOEFF_NORMED)
                sim_DF = cv.matchTemplate(given_figs["D"], given_figs["F"], cv.TM_CCOEFF_NORMED)

                sim_BC = cv.matchTemplate(given_figs["B"], given_figs["C"], cv.TM_CCOEFF_NORMED)
                sim_EF = cv.matchTemplate(given_figs["E"], given_figs["F"], cv.TM_CCOEFF_NORMED)

                sim_AG = cv.matchTemplate(given_figs["A"], given_figs["G"], cv.TM_CCOEFF_NORMED)
                sim_BH = cv.matchTemplate(given_figs["B"], given_figs["H"], cv.TM_CCOEFF_NORMED)

                sim_DG = cv.matchTemplate(given_figs["D"], given_figs["G"], cv.TM_CCOEFF_NORMED)
                sim_EH = cv.matchTemplate(given_figs["E"], given_figs["H"], cv.TM_CCOEFF_NORMED)

                sim_AE = cv.matchTemplate(given_figs["A"], given_figs["E"], cv.TM_CCOEFF_NORMED)

                if (sim_AC > 0.85 or sim_DF > 0.85) and (A_contour_areas_counter == C_contour_areas_counter and D_contour_areas_counter == F_contour_areas_counter)  and (1.11 >= (A_bpx/C_bpx) >= 0.90 and 1.11 >= (D_bpx/F_bpx) >= 0.90):
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["G"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            return int(option_fig)

                elif (sim_BC > 0.85 or sim_EF > 0.85) and (B_contour_areas_counter == C_contour_areas_counter and E_contour_areas_counter == F_contour_areas_counter)  and (1.11 >= (B_bpx/C_bpx) >= 0.90 and 1.11 >= (E_bpx/F_bpx) >= 0.90):
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["H"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            return int(option_fig)

                elif (sim_AG > 0.85 or sim_BH > 0.85) and (A_contour_areas_counter == G_contour_areas_counter and B_contour_areas_counter == H_contour_areas_counter) and (1.11 >= (A_bpx/G_bpx) >= 0.90 and 1.11 >= (B_bpx/H_bpx) >= 0.90):
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["C"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            return int(option_fig)

                elif (sim_DG > 0.85 or sim_EH > 0.85) and (D_contour_areas_counter == G_contour_areas_counter and E_contour_areas_counter == H_contour_areas_counter) and (1.11 >= (D_bpx/G_bpx) >= 0.90 and 1.11 >= (E_bpx/H_bpx) >= 0.90):
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["F"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            return int(option_fig)

                elif sim_AE > 0.85 and A_contour_areas_counter == E_contour_areas_counter and 1.11 >= (A_bpx/E_bpx) >= 0.90:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(given_figs["E"], option_fig_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            return int(option_fig)

            # Testing for Reflection
            def ThreeByThreeReflect(given_figs, option_figs):

                A_flip_y = cv.flip(given_figs["A"], 1)
                A_flip_x = cv.flip(given_figs["A"], 0)
                C_flip_x = cv.flip(given_figs["C"], 0)
                G_flip_y = cv.flip(given_figs["G"], 1)
                sim_reflect_AC = cv.matchTemplate(A_flip_y, given_figs["C"], cv.TM_CCOEFF_NORMED)
                sim_reflect_AG = cv.matchTemplate(A_flip_x, given_figs["G"], cv.TM_CCOEFF_NORMED)

                if sim_reflect_AC > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(G_flip_y, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

                elif sim_reflect_AG > 0.95:
                    for option_fig, option_fig_img in option_figs.items():
                        if cv.matchTemplate(C_flip_x, option_fig_img, cv.TM_CCOEFF_NORMED) > 0.95:
                            return int(option_fig)

            # Testing for Change in Area of a Shape
            def ThreeByThreeAreaChange(given_figs, option_figs):

                def area_compare_ratio(contour_areas_1, contour_areas_2):
                    similar_areas_count = 0
                    similar_areas_index_1 = []
                    similar_areas_index_2 = []
                    different_areas_count = 0
                    different_areas_index = []
                    different_areas_ratio = 0
                    if len(contour_areas_1) == len(contour_areas_2):
                        for area1 in contour_areas_1:
                            for area2 in contour_areas_2:
                                if abs(area1 - area2) <= 100:
                                    similar_areas_count += 1
                                    similar_areas_index_1.append(contour_areas_1.index(area1))
                                    similar_areas_index_2.append(contour_areas_2.index(area2))
                        for x in range(len(contour_areas_1)):
                            for y in range(len(contour_areas_2)):
                                if x not in similar_areas_index_1 and y not in similar_areas_index_2:
                                    different_areas_count += 1
                                    different_areas_index.append(x)
                                    if contour_areas_2[y]>0:
                                        different_areas_ratio = contour_areas_1[x] / contour_areas_2[y]
                    return different_areas_ratio

                different_area_ratio_EF = area_compare_ratio(E_contour_areas, F_contour_areas)
                different_area_ratio_EH = area_compare_ratio(E_contour_areas, H_contour_areas)

                for option_fig, option_img in option_figs.items():

                        option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                        option_contour_areas = contour_areas(option_contours, option_hierarchy)

                        different_area_ratio_Hoption = area_compare_ratio(H_contour_areas, option_contour_areas)
                        different_area_ratio_Foption = area_compare_ratio(F_contour_areas, option_contour_areas)

                        if different_area_ratio_EF != 0 and different_area_ratio_EH != 0:
                            if 1 - (abs(different_area_ratio_Hoption - different_area_ratio_EF)/different_area_ratio_EF) >= 0.90:
                                return int(option_fig)
                            elif 1 - (abs(different_area_ratio_Foption - different_area_ratio_EH)/different_area_ratio_EF) >= 0.90:
                                return int(option_fig)

            # Testing for Change in Number of a Shape
            def OuterShapeChange(given_figs, option_figs):

                def IBP(img1, img2):
                    ibpx = 0
                    for x in range(len(img1)):
                        for y in range(len(img1[0])):
                            if img1[x][y] == 255 and img2[x][y] == 255:
                                ibpx += 1
                    return ibpx
                if A_bpx > 0:
                    if A_contour_areas_counter > E_contour_areas_counter and 1.05 >= (IBP(given_figs['A'], given_figs['E']))/E_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            option_bpx = np.sum(option_img == 255)
                            if E_contour_areas_counter > option_contour_areas_counter and 1.05 >= (IBP(given_figs['E'], option_img))/option_bpx >= 0.95:
                                return int(option_fig)

                    elif A_contour_areas_counter < E_contour_areas_counter and 1.05 >= (IBP(given_figs['A'], given_figs['E']))/A_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            if E_contour_areas_counter < option_contour_areas_counter and 1.05 >= (IBP(given_figs['E'], option_img))/E_bpx >= 0.95:
                                return int(option_fig)

                    elif B_contour_areas_counter > C_contour_areas_counter and 1.05 >= (IBP(given_figs['B'], given_figs['C']))/C_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            option_bpx = np.sum(option_img == 255)
                            if H_contour_areas_counter > option_contour_areas_counter and 1.05 >= (IBP(given_figs['H'], option_img))/option_bpx >= 0.95:
                                return int(option_fig)

                    elif B_contour_areas_counter < C_contour_areas_counter and 1.05 >= (IBP(given_figs['B'], given_figs['C']))/B_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            if H_contour_areas_counter < option_contour_areas_counter and 1.05 >= (IBP(given_figs['H'], option_img))/H_bpx >= 0.95:
                                return int(option_fig)

                    elif D_contour_areas_counter > G_contour_areas_counter and 1.05 >= (IBP(given_figs['D'], given_figs['G']))/G_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            option_bpx = np.sum(option_img == 255)
                            if F_contour_areas_counter > option_contour_areas_counter and 1.05 >= (IBP(given_figs['F'], option_img))/option_bpx >= 0.95:
                                return int(option_fig)

                    elif B_contour_areas_counter < C_contour_areas_counter and 1.05 >= (IBP(given_figs['D'], given_figs['G']))/B_bpx >= 0.95:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            if F_contour_areas_counter < option_contour_areas_counter and 1.05 >= (IBP(given_figs['F'], option_img))/F_bpx >= 0.95:
                                return int(option_fig)

            def IBP(img1, img2):
                ibpx = 0
                for x in range(len(img1)):
                    for y in range(len(img1[0])):
                        if img1[x][y] == 255 and img2[x][y] == 255:
                            ibpx += 1
                return ibpx

            def ShapeNumberChange(given_figs, option_figs):

                if A_bpx > 0 and A_contour_areas_counter > 0:
                    AC_number_ratio = C_contour_areas_counter/A_contour_areas_counter
                    AC_dpr = C_bpx/A_bpx
                    AG_number_ratio = G_contour_areas_counter/A_contour_areas_counter
                    AG_dpr = G_bpx/A_bpx

                    AC_dpd = abs(C_bpx - A_bpx)
                    DF_dpd = abs(D_bpx - F_bpx)
                    AG_dpd = abs(G_bpx - A_bpx)
                    BH_dpd = abs(H_bpx - H_bpx)
                    possible_answers = []

                    if abs(AC_number_ratio - AC_dpr) <= 0.1 and C_contour_areas_counter != A_contour_areas_counter:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            option_bpx = np.sum(option_img == 255)
                            Goption_number_ratio = option_contour_areas_counter/G_contour_areas_counter
                            Goption_dpr = option_bpx/G_bpx
                            if abs(Goption_number_ratio - Goption_dpr) <= 0.15 and Goption_number_ratio == AC_number_ratio:
                                possible_answers.append(option_fig)
                        if len(possible_answers) > 1:
                            for fig in possible_answers:
                                Goption_ipr = IBP(given_figs['G'], option_figs[fig]) / G_bpx
                                if 1.11 >= Goption_ipr >= 0.9:
                                    return int(fig)
                        elif len(possible_answers) == 1:
                            return int(possible_answers[0])

                    elif abs(AG_number_ratio - AG_dpr) <= 0.1 and G_contour_areas_counter != A_contour_areas_counter:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_contour_areas_counter = len(option_contour_areas)
                            option_bpx = np.sum(option_img == 255)
                            Coption_number_ratio = option_contour_areas_counter/C_contour_areas_counter
                            Coption_dpr = option_bpx/C_bpx
                            if abs(Coption_number_ratio - Coption_dpr) <= 0.15 and Coption_number_ratio == AG_number_ratio:
                                possible_answers.append(option_fig)
                        if len(possible_answers) > 1:
                            for fig in possible_answers:
                                Coption_ipr = IBP(given_figs['C'], option_figs[fig]) / C_bpx
                                if 1.11 >= Coption_ipr >= 0.9:
                                    return int(fig)
                        elif len(possible_answers) == 1:
                            return int(possible_answers[0])


                    if abs(AC_dpd - DF_dpd) <= 50 and C_contour_areas_counter != A_contour_areas_counter:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_bpx = np.sum(option_img == 255)
                            Goption_dpd = abs(G_bpx - option_bpx)
                            if abs(Goption_dpd - AC_dpd) < 50:
                                possible_answers.append(option_fig)
                        if len(possible_answers) > 1:
                            for fig in possible_answers:
                                Goption_ipr = IBP(given_figs['G'], option_figs[fig]) / G_bpx
                                if 1.11 >= Goption_ipr >= 0.9:
                                    return int(fig)
                        elif len(possible_answers) == 1:
                            return int(possible_answers[0])

                    elif abs(AG_dpd - BH_dpd) <= 50 and G_contour_areas_counter != A_contour_areas_counter:
                        for option_fig, option_img in option_figs.items():
                            option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
                            option_contour_areas = contour_areas(option_contours, option_hierarchy)
                            option_bpx = np.sum(option_img == 255)
                            Coption_dpd = abs(C_bpx - option_bpx)
                            if abs(Coption_dpd - AG_dpd) < 50:
                                possible_answers.append(option_fig)
                        if len(possible_answers) > 1:
                            for fig in possible_answers:
                                Coption_ipr = IBP(given_figs['C'], option_figs[fig]) / C_bpx
                                if 1.11 >= Coption_ipr >= 0.9:
                                    return int(fig)
                        elif len(possible_answers) == 1:
                            return int(possible_answers[0])

            def ContourCount(given_figs, option_figs):

                if (not(1.05 >= (A_bpx/B_bpx) >= 0.95) and not(1.05 >= (B_bpx/C_bpx) >= 0.95)) and (A_contour_areas_counter == B_contour_areas_counter == C_contour_areas_counter) and (A_contour_areas_counter != E_contour_areas_counter and A_contour_areas_counter != D_contour_areas_counter and B_contour_areas_counter!=F_contour_areas_counter and D_contour_areas_counter!=G_contour_areas_counter and A_contour_areas_counter!=G_contour_areas_counter and D_contour_areas_counter!=H_contour_areas_counter):
                    for option_fig, option_img in option_figs.items():
                        option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,
                                                                            cv.CHAIN_APPROX_NONE)
                        option_contour_areas = contour_areas(option_contours, option_hierarchy)
                        option_contour_areas_counter = len(option_contour_areas)
                        option_bpx = np.sum(option_img == 255)
                        if (not (1.05 >= (G_bpx / H_bpx) >= 0.95) and not (1.05 >= (H_bpx / option_bpx) >= 0.95)) and (G_contour_areas_counter == H_contour_areas_counter == option_contour_areas_counter):
                            return int(option_fig)

                elif (not(1.05 >= (B_bpx/F_bpx) >= 0.95) and not(1.05 >= (A_bpx/E_bpx) >= 0.95) and not(1.05 >= (D_bpx/H_bpx) >= 0.95)) and (A_contour_areas_counter == E_contour_areas_counter and B_contour_areas_counter == F_contour_areas_counter and D_contour_areas_counter == H_contour_areas_counter) and (A_contour_areas_counter != B_contour_areas_counter and A_contour_areas_counter != D_contour_areas_counter and B_contour_areas_counter!=C_contour_areas_counter and A_contour_areas_counter!=C_contour_areas_counter and D_contour_areas_counter!=G_contour_areas_counter and A_contour_areas_counter!=G_contour_areas_counter):
                    for option_fig, option_img in option_figs.items():
                        option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,
                                                                            cv.CHAIN_APPROX_NONE)
                        option_contour_areas = contour_areas(option_contours, option_hierarchy)
                        option_contour_areas_counter = len(option_contour_areas)
                        option_bpx = np.sum(option_img == 255)
                        if (not (1.05 >= (A_bpx / option_bpx) >= 0.95) and not (1.05 >= (E_bpx / option_bpx) >= 0.95)) and (A_contour_areas_counter == E_contour_areas_counter == option_contour_areas_counter):
                            return int(option_fig)

                elif (not(1.05 >= (A_bpx/D_bpx) >= 0.95) and not(1.05 >= (D_bpx/G_bpx) >= 0.95)) and (A_contour_areas_counter == D_contour_areas_counter == G_contour_areas_counter) and (A_contour_areas_counter != E_contour_areas_counter and A_contour_areas_counter != B_contour_areas_counter and A_contour_areas_counter != C_contour_areas_counter and B_contour_areas_counter!=C_contour_areas_counter and B_contour_areas_counter!=F_contour_areas_counter and D_contour_areas_counter!=H_contour_areas_counter):
                    for option_fig, option_img in option_figs.items():
                        option_contours, option_hierarchy = cv.findContours(option_img, cv.RETR_CCOMP,
                                                                            cv.CHAIN_APPROX_NONE)
                        option_contour_areas = contour_areas(option_contours, option_hierarchy)
                        option_contour_areas_counter = len(option_contour_areas)
                        option_bpx = np.sum(option_img == 255)
                        if (not (1.05 >= (C_bpx / option_bpx) >= 0.95) and not (1.05 >= (F_bpx / option_bpx) >= 0.95)) and (C_contour_areas_counter == F_contour_areas_counter == option_contour_areas_counter):
                            return int(option_fig)

            # Testing for Logic Operations
            def PixelLogic(given_figs, option_figs):

                log_A = given_figs['A']
                log_B = given_figs['B']
                log_C = given_figs['C']
                log_D = given_figs['D']
                log_E = given_figs['E']
                log_F = given_figs['F']
                log_G = given_figs['G']
                log_H = given_figs['H']

                closest_options_and = dict()
                closest_options_or = dict()
                closest_options_xor = dict()

                and_AB = cv.bitwise_and(log_A, log_B)
                sim_and_ABC = cv.matchTemplate(and_AB, log_C, cv.TM_CCOEFF_NORMED)
                and_DE = cv.bitwise_and(log_D, log_E)
                sim_and_DEF = cv.matchTemplate(and_DE, log_F, cv.TM_CCOEFF_NORMED)
                and_GH = cv.bitwise_and(log_G, log_H)
                and_AD = cv.bitwise_and(log_A, log_D)
                sim_and_ADG = cv.matchTemplate(and_AD, log_G, cv.TM_CCOEFF_NORMED)
                and_BE = cv.bitwise_and(log_B, log_E)
                sim_and_BEH = cv.matchTemplate(and_BE, log_H, cv.TM_CCOEFF_NORMED)
                and_CF = cv.bitwise_and(log_C, log_F)

                if sim_and_ABC > 0.90 or sim_and_DEF > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            closest_options_and[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_and.items():
                        if val == max(closest_options_and.values()):
                            return int(key)

                elif sim_and_ADG > 0.90 or sim_and_BEH > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if cv.matchTemplate(and_CF, option_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            closest_options_and[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_and.items():
                        if val == max(closest_options_and.values()):
                            return int(key)

                or_AB = cv.bitwise_or(log_A, log_B)
                sim_or_ABC = cv.matchTemplate(or_AB, log_C, cv.TM_CCOEFF_NORMED)
                or_DE = cv.bitwise_or(log_D, log_E)
                sim_or_DEF = cv.matchTemplate(or_DE, log_F, cv.TM_CCOEFF_NORMED)
                or_GH = cv.bitwise_or(log_G, log_H)
                or_AD = cv.bitwise_or(log_A, log_D)
                sim_or_ADG = cv.matchTemplate(or_AD, log_G, cv.TM_CCOEFF_NORMED)
                or_BE = cv.bitwise_or(log_B, log_E)
                sim_or_BEH = cv.matchTemplate(or_BE, log_H, cv.TM_CCOEFF_NORMED)
                or_CF = cv.bitwise_or(log_C, log_F)

                if sim_or_ABC > 0.90 or sim_or_DEF > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if cv.matchTemplate(or_GH, option_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            closest_options_or[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_or.items():
                        if val == max(closest_options_or.values()):
                            return int(key)

                elif sim_or_ADG > 0.90 or sim_or_BEH > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if cv.matchTemplate(or_CF, option_img, cv.TM_CCOEFF_NORMED) > 0.85:
                            closest_options_or[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_or.items():
                        if val == max(closest_options_or.values()):
                            return int(key)

                xor_AB = cv.bitwise_xor(log_A, log_B)
                sim_xor_ABC = abs(cv.matchTemplate(xor_AB, log_C, cv.TM_CCOEFF_NORMED))
                xor_DE = cv.bitwise_xor(log_D, log_E)
                sim_xor_DEF = abs(cv.matchTemplate(xor_DE, log_F, cv.TM_CCOEFF_NORMED))
                xor_GH = cv.bitwise_xor(log_G, log_H)
                xor_AD = cv.bitwise_xor(log_A, log_D)
                sim_xor_ADG = abs(cv.matchTemplate(xor_AD, log_G, cv.TM_CCOEFF_NORMED))
                xor_BE = cv.bitwise_xor(log_B, log_E)
                sim_xor_BEH = abs(cv.matchTemplate(xor_BE, log_H, cv.TM_CCOEFF_NORMED))
                xor_CF = cv.bitwise_xor(log_C, log_F)

                if sim_xor_ABC > 0.90 or sim_xor_DEF > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if abs(cv.matchTemplate(xor_GH, option_img, cv.TM_CCOEFF_NORMED)) > 0.85:
                            closest_options_xor[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_xor.items():
                        if val == max(closest_options_xor.values()):
                            return int(key)
                elif sim_xor_ADG > 0.90 or sim_xor_BEH > 0.90:
                    for option_fig, option_img in option_figs.items():
                        if abs(cv.matchTemplate(xor_CF, option_img, cv.TM_CCOEFF_NORMED)) > 0.85:
                            closest_options_xor[option_fig] = cv.matchTemplate(and_GH, option_img, cv.TM_CCOEFF_NORMED)
                    for key, val in closest_options_xor.items():
                        if val == max(closest_options_xor.values()):
                            return int(key)

            def PixelArit(given_figs, option_figs):
                pix_diff_AB = abs(A_bpx - B_bpx)
                pix_diff_DE = abs(D_bpx - E_bpx)
                pix_diff_GH = abs(G_bpx - H_bpx)

                pix_diff_AD = abs(A_bpx - D_bpx)
                pix_diff_BE = abs(B_bpx - E_bpx)
                pix_diff_CF = abs(G_bpx - H_bpx)

                pix_add_AB = abs(A_bpx + B_bpx)
                pix_add_DE = abs(D_bpx + E_bpx)
                pix_add_GH = abs(G_bpx + H_bpx)

                pix_add_AD = abs(A_bpx + D_bpx)
                pix_add_BE = abs(B_bpx + E_bpx)
                pix_add_CF = abs(G_bpx + H_bpx)

                possible_answers_diff = []
                possible_answers_add = []

                if (1.05 >= pix_diff_AB / C_bpx >= 0.95) or (1.05 >= pix_diff_DE / F_bpx >= 0.95):
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 255)
                        if 1.05 >= pix_diff_GH / option_bpx >= 0.95:
                            possible_answers_diff.append(option_fig)
                    for fig in possible_answers_diff:
                        for given_img in given_figs.values():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.90 and fig in possible_answers_diff:
                                possible_answers_diff.remove(fig)
                    if len(possible_answers_diff) == 1:
                        return int(possible_answers_diff[0])

                elif (1.05 >= pix_diff_AD / G_bpx >= 0.95) or (1.05 >= pix_diff_BE / H_bpx >= 0.95):
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 0)
                        if 1.05 >= pix_diff_CF / option_bpx >= 0.95:
                            possible_answers_diff.append(option_fig)
                    for fig in possible_answers_diff:
                        for given_img in given_figs.values():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.90 and fig in possible_answers_diff:
                                possible_answers_diff.remove(fig)
                    if len(possible_answers_diff) == 1:
                        return int(possible_answers_diff[0])

                if (1.05 >= pix_add_AB / C_bpx >= 0.95) or (1.05 >= pix_add_DE / F_bpx >= 0.95):
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 255)
                        if 1.05 >= pix_add_GH / option_bpx >= 0.95:
                            possible_answers_add.append(option_fig)
                    for fig in possible_answers_add:
                        for given_img in given_figs.values():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.90 and fig in possible_answers_add:
                                possible_answers_add.remove(fig)
                    if len(possible_answers_add) == 1:
                        return int(possible_answers_add[0])

                elif (1.05 >= pix_add_AD / G_bpx >= 0.95) or (1.05 >= pix_add_BE / H_bpx >= 0.95):
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 0)
                        if 1.05 >= pix_add_CF / option_bpx >= 0.95:
                            possible_answers_add.append(option_fig)
                    for fig in possible_answers_add:
                        for given_img in given_figs.values():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.90 and fig in possible_answers_add:
                                possible_answers_add.remove(fig)
                    if len(possible_answers_add) == 1:
                        return int(possible_answers_add[0])

            # Testing for Pixel Patterns
            def PixelCount(given_figs, option_figs):

                row1sum = A_bpx + B_bpx + C_bpx
                row2sum = D_bpx + E_bpx + F_bpx

                col1sum = A_bpx + D_bpx + G_bpx
                col2sum = B_bpx + E_bpx + H_bpx

                closest_options = dict()

                if 1.02 >= row1sum/row2sum >= 0.98:
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 255)
                        row3sum = G_bpx + H_bpx + option_bpx
                        if 1.05 >= row3sum/row1sum >= 0.95:
                            closest_options[option_fig] = abs(row3sum - row1sum)
                    fig_keys_1 = list(closest_options.keys())
                    for fig in fig_keys_1:
                        for given_key, given_img in given_figs.items():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.95 and fig in closest_options.keys():
                                del closest_options[fig]
                    for key, val in closest_options.items():
                        if val == min(closest_options.values()):
                            return int(key)

                elif 1.02 >= col1sum/col2sum >= 0.98:
                    for option_fig, option_img in option_figs.items():
                        option_bpx = np.sum(option_img == 255)
                        col3sum = C_bpx + F_bpx + option_bpx
                        if 1.05 >= col3sum/col1sum >= 0.95:
                            closest_options[option_fig] = abs(col3sum - col1sum)
                    fig_keys_2 = list(closest_options.keys())
                    for fig in fig_keys_2:
                        for given_img in given_figs.values():
                            if cv.matchTemplate(option_figs[fig], given_img, cv.TM_CCOEFF_NORMED) >= 0.95 and fig in closest_options.keys():
                                del closest_options[fig]
                    for key, val in closest_options.items():
                        if val == min(closest_options.values()):
                            return int(key)

            def PixelChange(given_figs, option_figs):
                AE_dpr = abs(A_dpr - E_dpr)
                CF_dpr = abs(C_dpr - F_dpr)
                GH_dpr = abs(G_dpr - H_dpr)
                AC_dpr = abs(A_dpr - C_dpr)
                AG_dpr = abs(A_dpr - G_dpr)

                for option_fig, option_img in option_figs.items():
                    option_bpx = np.sum(option_img == 255)
                    option_tpx = np.sum(option_img == 255) + np.sum(option_img == 0)
                    option_dpr = option_bpx/option_tpx
                    if option_dpr > 0:
                        if A_bpx > C_bpx and 1.11 >= (G_dpr - AC_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif A_bpx < C_bpx and 1.11 >= (G_dpr + AC_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        if A_bpx > G_bpx and 1.11 >= (C_dpr - AG_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif A_bpx < G_bpx and 1.11 >= (C_dpr + AG_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        if A_bpx > E_bpx and 1.11 >= (E_dpr - AE_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif A_bpx < E_bpx and 1.11 >= (E_dpr + AE_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif C_bpx > F_bpx and 1.11 >= (F_dpr - CF_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif C_bpx < F_bpx and 1.11 >= (F_dpr + CF_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif G_bpx > H_bpx and 1.11 >= (H_dpr - GH_dpr)/option_dpr >= 0.90:
                            return int(option_fig)
                        elif G_bpx < H_bpx and 1.11 >= (H_dpr + GH_dpr)/option_dpr >= 0.90:
                            return int(option_fig)

            def FallBack(given_figs, option_figs):
                AE_dpr = abs(A_dpr - E_dpr)
                CF_dpr = abs(C_dpr - F_dpr)
                GH_dpr = abs(G_dpr - H_dpr)
                AC_dpr = abs(A_dpr - C_dpr)
                AG_dpr = abs(A_dpr - G_dpr)

                closest_options = dict()

                for option_fig, option_img in option_figs.items():
                    option_bpx = np.sum(option_img == 255)
                    option_tpx = np.sum(option_img == 255) + np.sum(option_img == 0)
                    option_dpr = option_bpx / option_tpx
                    if option_dpr > 0:
                        if A_bpx > E_bpx or C_bpx > F_bpx or G_bpx > H_bpx or A_bpx > C_bpx or A_bpx > G_bpx:
                            closest_options[option_fig] = abs(min((E_dpr - AE_dpr)/option_dpr, (F_dpr - CF_dpr)/option_dpr, (H_dpr - GH_dpr)/option_dpr, (G_dpr - AC_dpr)/option_dpr, (C_dpr - AG_dpr)/option_dpr) - 1)
                        else:
                            closest_options[option_fig] = abs(min((E_dpr + AE_dpr)/option_dpr, (F_dpr + CF_dpr)/option_dpr, (H_dpr + GH_dpr)/option_dpr, (G_dpr + AC_dpr)/option_dpr, (C_dpr + AG_dpr)/option_dpr)- 1)
                for key, val in closest_options.items():
                    if val == min(closest_options.values()):
                        return int(key)

            ThreeByThreeEqualityAnswer = ThreeByThreeEquality(given_figs, option_figs)
            if type(ThreeByThreeEqualityAnswer) == int:
                return ThreeByThreeEqualityAnswer
            else:
                ThreeByThreeReflectAnswer = ThreeByThreeReflect(given_figs, option_figs)
                if type(ThreeByThreeReflectAnswer) == int:
                    return ThreeByThreeReflectAnswer
                else:
                    ThreeByThreeAreaChangeAnswer = ThreeByThreeAreaChange(given_figs, option_figs)
                    if type(ThreeByThreeAreaChangeAnswer) == int:
                        return ThreeByThreeAreaChangeAnswer
                    else:
                        OuterShapeChangeAnswer = OuterShapeChange(given_figs, option_figs)
                        if type(OuterShapeChangeAnswer) == int:
                            return OuterShapeChangeAnswer
                        else:
                            ShapeNumberChangeAnswer = ShapeNumberChange(given_figs, option_figs)
                            if type(ShapeNumberChangeAnswer) == int:
                                return ShapeNumberChangeAnswer
                            else:
                                ContourCountAnswer = ContourCount(given_figs, option_figs)
                                if type(ContourCountAnswer) == int:
                                    return ContourCountAnswer
                                else:
                                    given_figs_log = dict()
                                    option_figs_log = dict()

                                    for fig in problem.figures:
                                        if fig in "ABCDEFGH":
                                            img = cv.imread(problem.figures[fig].visualFilename, cv.IMREAD_GRAYSCALE)
                                            ret, given_figs_log[fig] = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
                                        else:
                                            img = cv.imread(problem.figures[fig].visualFilename, cv.IMREAD_GRAYSCALE)
                                            ret, option_figs_log[fig] = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
                                    PixelLogicAnswer = PixelLogic(given_figs_log, option_figs_log)
                                    if type(PixelLogicAnswer) == int:
                                        return PixelLogicAnswer
                                    else:
                                        PixelAritAnswer = PixelArit(given_figs, option_figs)
                                        if type(PixelAritAnswer) == int:
                                            return PixelAritAnswer
                                        else:
                                            PixelCountAnswer = PixelCount(given_figs, option_figs)
                                            if type(PixelCountAnswer) == int:
                                                return PixelCountAnswer
                                            else:
                                                PixelChangeAnswer = PixelChange(given_figs, option_figs)
                                                if type(PixelChangeAnswer) == int:
                                                    return PixelChangeAnswer

                                                else:
                                                    FallbackAnswer = FallBack(given_figs, option_figs)
                                                    if type(FallbackAnswer) == int:
                                                        return FallbackAnswer
