from search_engine_mechanism.infra.RankingMechanism import RankingMechanism


class SearchTermsOption:
    def __init__(self, database_path):
        self.database_path = database_path

    def getSearchTermOptions(self, search_term):
        ranking_mechanism = RankingMechanism(self.database_path)
        ranking_parameters = ranking_mechanism.get_ranking_parameters()

        ranking_mechanism.commit_and_close()

        # Return the sorted search term options
        return sorted(search_term, key=lambda x: x['total_grade'], reverse=True)
