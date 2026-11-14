// Loaded only after explicit device-compute and download consent.
import {CreateWebWorkerMLCEngine, prebuiltAppConfig, deleteModelAllInfoInCache} from 'https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.88/lib/index.js';

export const MODEL_ID = 'Qwen2.5-0.5B-Instruct-q4f16_1-MLC';
export const MODEL_REVISION = '32ff081fe7e4dfe4ffb167b94c66fdf11e02b8ad';
let worker;
const record = prebuiltAppConfig.model_list.find(model => model.model_id === MODEL_ID);
if (!record) throw new Error('Pinned model is not present in this WebLLM release.');
const appConfig = {model_list: [{...record, model: `https://huggingface.co/mlc-ai/${MODEL_ID}/resolve/${MODEL_REVISION}/`, overrides: {...record.overrides, context_window_size:4096}}], useIndexedDBCache: true};

export async function load(onProgress) {
  worker = new Worker(new URL('./model-worker.mjs', import.meta.url), {type:'module'});
  try {
    const failure = new Promise((_,reject) => worker.addEventListener('error', event=>reject(new Error(event.message || 'Model worker failed to load.')), {once:true}));
    return await Promise.race([CreateWebWorkerMLCEngine(worker, MODEL_ID, {appConfig, initProgressCallback:onProgress}, {context_window_size:4096}),failure]);
  } catch (error) {
    stop();
    throw error;
  }
}
export function stop() { if (worker) worker.terminate(); worker = null; }
export async function clearModelCache() { await deleteModelAllInfoInCache(MODEL_ID, appConfig); }
