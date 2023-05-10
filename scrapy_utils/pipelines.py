
class AddMetadataPipeline:
    def process_item(self, item, spider):
        item.job_id = spider.job_id
        item.spider = spider.name
        return item
