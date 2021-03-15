introParagraph =    ('Welcome to the Kramaral Content Generator Service! Please use '
                    'the options below to select one or more types of content requested and '
                    'type the keywords for your request into the fields below. For details on '
                    'the types of output available, hover over the ToolTip ? Icon next to each option. Click the' 
                    'Submit button to then quickly recieve your new information!')

mainTopicToolTip = ('This entry field is for your main keyword - The content generator will '
                    'use this keyword to seek out a page on Wikipedia  or an Amazon category depending on'
                    ' the option selected. If content does not exist for that topic in the '
                    'selected search option, the search may not return content')

subTopicToolTip = ('This entry field is for your sub-topic keyword - The content generator will '
                    'use this keyword to seek out a paragraph on Wikipedia  or Amazon products depending on'
                    ' the option selected. If content does not exist for that topic in the '
                    'selected search option, the search may not return content')

contentOptionToolTip = ('This check box will add a field to output, and then search wikipedia for a page relating to the' 
                        ' main keyword, and a paragraph within that page containing both the main keyword and sub-topic'
                        ' keyword. If no page exists for the main keyword, or a paragraph with both keywords is not' 
                        ' found within that page, the output will state that no results were found')

shoppingOptionToolTip = ('This check box will add a field to the output for top 10 Amazon product results relating'
                         ' to the provided keyword pair. The main keyword will be used as the product category,'
                         ' and the sub-topic will be used as the product type. If fewer than 10 products are found, '
                         'the output returned may contain fewer results or a message stating no results found.')