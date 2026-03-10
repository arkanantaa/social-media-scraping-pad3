
# Scraping Social Media PAD 3

Scraping dilakukan dengan [gallery-dl](https://github.com/mikf/gallery-dl) di berbagai media sosial menggunakan search berdasarkan hashtag. Data yang diperoleh nantinya akan dilakukan cleaning dan labeling.  

## Safe
1. Disney Cartoon
```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/disneyart/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/cartoon/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

## Unsafe
1. Racism
```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/racism/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

2. Jokes Homo
```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/jomok/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/ambatukam/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/lgbt/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

3. Dark Humor/Jokes
```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/darkjokes/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```

4. War Related
```
gallery-dl --range 1-300 `  
>>   --cookies-from-browser firefox `
>>   --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" `
>>   --write-metadata --write-tags `
>>   --sleep 3-7 --sleep-request 10-20 `
>>   "https://www.instagram.com/explore/tags/missile/" `
>>   --filter "extension in ('jpg', 'jpeg', 'png', 'webp')"
```