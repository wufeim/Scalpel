from scalpel import ScalpelDashboard, ScalpelPage, ScalpelTable


def test():
    table = ScalpelTable(columns=['query', 'return', 'dist', 'hm', 'pred', 'prior', 'complete',
                                  'entropy score', 'dist score', 'final_score'])
    table.append_row([
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/incomplete_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/return_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/dist_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/hm_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/pred_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/prior_0.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/complete_0.png',
        1.000, 1.000, 1.000
    ])
    table.append_row([
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/incomplete_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/return_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/dist_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/hm_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/pred_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/prior_1.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/complete_1.png',
        0.998, 0.923, 0.922
    ])
    table.append_row([
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/incomplete_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/return_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/dist_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/hm_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/pred_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/prior_2.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/complete_2.png',
        1.000, 0.850, 0.850
    ])
    table.append_row([
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/incomplete_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/return_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/dist_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/hm_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/pred_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/prior_3.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/complete_3.png',
        0.986, 0.652, 0.643
    ])
    table.append_row([
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/incomplete_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/return_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/dist_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/hm_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/pred_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/prior_4.png',
        '/Users/wufeim/Downloads/suggestive_completion/single_0000001/output/complete_4.png',
        0.877, 0.652, 0.572
    ])

    dashboard = ScalpelDashboard(title='Suggestive Completion System')
    dashboard.add_text('0000001.png', style='p')
    dashboard.add_component(table)
    dashboard.save_html('results.html')


if __name__ == '__main__':
    test()
