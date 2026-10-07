import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    sourceUrl: z.string().url(),
    sourceName: z.string(),
    tags: z.array(z.string()).default([]),
    aiGenerated: z.boolean().default(true),
  }),
});

export const collections = { articles };
