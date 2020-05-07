import pandas as pd

df_tag = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")
df_btag = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv")
df_b=pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")

re_sc='.*sci.*fi.*'
re_hor='.*horror.*'
re_come='.*comedy.*'
re_bio='.*biogra.*|.*memoir.*'
re_romance='.*romanc.*|.*romantic.*'
re_adv='.*advent.*'
re_comi='.*comic.*'
re_poet='.*poetry.*'

scifi=df_tag[df_tag['tag_name'].str.match(re_sc)]
horor=df_tag[df_tag['tag_name'].str.match(re_hor)]
comedy=df_tag[df_tag['tag_name'].str.match(re_come)]
bio=df_tag[df_tag['tag_name'].str.match(re_bio)]
romance=df_tag[df_tag['tag_name'].str.match(re_romance)]
adventure=df_tag[df_tag['tag_name'].str.match(re_adv)]
comics=df_tag[df_tag['tag_name'].str.match(re_comi)]
poetry=df_tag[df_tag['tag_name'].str.match(re_poet)]



scifi = pd.merge(left=df_btag, right=scifi)
horor = pd.merge(left=df_btag, right=horor)
comedy = pd.merge(left=df_btag, right=comedy)
bio = pd.merge(left=df_btag, right=bio)
romance = pd.merge(left=df_btag, right=romance)
adventure = pd.merge(left=df_btag, right=adventure)
comics = pd.merge(left=df_btag, right=comics)
poetry = pd.merge(left=df_btag, right=poetry)


scifi = pd.merge(left=df_b, right=scifi)
horor = pd.merge(left=df_b, right=horor)
comedy = pd.merge(left=df_b, right=comedy)
bio = pd.merge(left=df_b, right=bio)
romance = pd.merge(left=df_b, right=romance)
adventure = pd.merge(left=df_b, right=adventure)
comics = pd.merge(left=df_b, right=comics)
poetry = pd.merge(left=df_b, right=poetry)



scifi.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
horor.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
comedy.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
bio.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
romance.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
adventure.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
comics.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
poetry.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)


scifi.dropna(subset=['isbn','original_title'], inplace=True)
horor.dropna(subset=['isbn','original_title'], inplace=True)
comedy.dropna(subset=['isbn','original_title'], inplace=True)
bio.dropna(subset=['isbn','original_title'], inplace=True)
romance.dropna(subset=['isbn','original_title'], inplace=True)
adventure.dropna(subset=['isbn','original_title'], inplace=True)
comics.dropna(subset=['isbn','original_title'], inplace=True)
poetry.dropna(subset=['isbn','original_title'], inplace=True)


scifi=scifi[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
horor=horor[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
comedy=comedy[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
bio=bio[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
romance=romance[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
adventure=adventure[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
comics=comics[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]
poetry=poetry[['goodreads_book_id','authors','isbn','original_title','average_rating','image_url']]



scifi.sort_values(by='average_rating',ascending=False,inplace=True)
horor.sort_values(by='average_rating',ascending=False,inplace=True)
comedy.sort_values(by='average_rating',ascending=False,inplace=True)
bio.sort_values(by='average_rating',ascending=False,inplace=True)
romance.sort_values(by='average_rating',ascending=False,inplace=True)
adventure.sort_values(by='average_rating',ascending=False,inplace=True)
comics.sort_values(by='average_rating',ascending=False,inplace=True)
poetry.sort_values(by='average_rating',ascending=False,inplace=True)


scifi=scifi[:1000]
horor=horor[:1000]
bio=bio[:1000]
romance=romance[:1000]
adventure=adventure[:1000]

print(scifi.count());
print(horor.count())
print(comedy.count())
print(bio.count())
print(romance.count())
print(adventure.count())
print(comics.count())
print(poetry.count())

pdList = [scifi,horor,comedy,bio,romance,adventure,comics,poetry]
new_df = pd.concat(pdList,ignore_index=True)
new_df.drop_duplicates(subset='goodreads_book_id', keep="first", inplace=True)
new_df.to_csv('./books_subset.csv')

scifi['genre']='scifi'
horor['genre']='horror'
comedy['genre']='comedy'
bio['genre']='bio'
romance['genre']='romance'
comics['genre']='comics'
adventure['genre']='adventure'
poetry['genre']='poetry'

scifi=scifi[['goodreads_book_id','genre']]
horor=horor[['goodreads_book_id','genre']]
comedy=comedy[['goodreads_book_id','genre']]
bio=bio[['goodreads_book_id','genre']]
romance=romance[['goodreads_book_id','genre']]
adventure=adventure[['goodreads_book_id','genre']]
comics=comics[['goodreads_book_id','genre']]
poetry=poetry[['goodreads_book_id','genre']]

pdList = [scifi,horor,comedy,bio,romance,adventure,comics,poetry]
new_df = pd.concat(pdList,ignore_index=True)
new_df.to_csv('./genre.csv')
